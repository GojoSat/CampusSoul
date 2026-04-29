import pygame
import sys
import random
import math

# 初始化 Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("动漫大乱斗 - Anime Brawl")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (160, 32, 240)
CYAN = (0, 255, 255)

clock = pygame.time.Clock()
FPS = 60

# ---------- 技能类 ----------
class Skill:
    def __init__(self, name, damage, energy_cost, cooldown, range_val, projectile_speed=0, aoe_radius=0):
        self.name = name
        self.damage = damage
        self.energy_cost = energy_cost
        self.cooldown = cooldown
        self.current_cooldown = 0
        self.range = range_val          # 作用距离（近战/远程）
        self.projectile_speed = projectile_speed
        self.aoe_radius = aoe_radius    # 范围爆炸半径

# ---------- 玩家角色 ----------
class Player:
    def __init__(self, x, y, name, color, hp, atk_damage, skill, speed=5):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.name = name
        self.color = color
        self.max_hp = hp
        self.hp = hp
        self.atk_damage = atk_damage
        self.skill = skill
        self.speed = speed
        self.energy = 100
        self.max_energy = 100
        self.alive = True
        self.attack_timer = 0
        self.facing = 1  # 1=右, -1=左

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        # 边界限制
        self.x = max(self.width//2, min(SCREEN_WIDTH - self.width//2, self.x))
        self.y = max(self.height//2, min(SCREEN_HEIGHT - self.height//2, self.y))
        if dx != 0:
            self.facing = 1 if dx > 0 else -1

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def use_skill(self):
        if self.skill.current_cooldown == 0 and self.energy >= self.skill.energy_cost:
            self.energy -= self.skill.energy_cost
            self.skill.current_cooldown = self.skill.cooldown
            return True
        return False

    def update(self):
        # 冷却递减
        if self.skill.current_cooldown > 0:
            self.skill.current_cooldown -= 1
        # 能量缓慢恢复
        if self.energy < self.max_energy:
            self.energy += 0.15  # 每帧恢复
        if self.attack_timer > 0:
            self.attack_timer -= 1

    def draw(self, screen):
        # 身体
        pygame.draw.rect(screen, self.color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))
        # 脸部方向指示
        eye_x_offset = 5 * self.facing
        pygame.draw.circle(screen, BLACK, (self.x + eye_x_offset, self.y - 5), 3)
        # 血条和能量条
        bar_width = 40
        hp_ratio = self.hp / self.max_hp
        energy_ratio = self.energy / self.max_energy
        pygame.draw.rect(screen, RED, (self.x - 20, self.y - 30, bar_width, 5))
        pygame.draw.rect(screen, GREEN, (self.x - 20, self.y - 30, bar_width * hp_ratio, 5))
        pygame.draw.rect(screen, BLUE, (self.x - 20, self.y - 24, bar_width, 4))
        pygame.draw.rect(screen, CYAN, (self.x - 20, self.y - 24, bar_width * energy_ratio, 4))
        # 名字
        font = pygame.font.SysFont("Arial", 12)
        name_surf = font.render(self.name, True, WHITE)
        screen.blit(name_surf, (self.x - name_surf.get_width()//2, self.y - 40))

# ---------- 弹幕类（远程技能） ----------
class Projectile:
    def __init__(self, x, y, direction, damage, speed, color, radius=5, lifetime=60):
        self.x = x
        self.y = y
        self.direction = direction
        self.damage = damage
        self.speed = speed
        self.color = color
        self.radius = radius
        self.lifetime = lifetime

    def update(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        self.lifetime -= 1
        return self.lifetime > 0 and (0 < self.x < SCREEN_WIDTH and 0 < self.y < SCREEN_HEIGHT)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# ---------- 敌人 ----------
class Enemy:
    def __init__(self, x, y, hp=50, damage=10, speed=2, color=RED):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.max_hp = hp
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.color = color
        self.attack_cooldown = 0
        self.alive = True

    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)
        if dist > 30:  # 不重叠时才移动
            self.x += (dx / dist) * self.speed
            self.y += (dy / dist) * self.speed

    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def attack_player(self, player):
        if self.attack_cooldown == 0:
            dist = math.hypot(self.x - player.x, self.y - player.y)
            if dist < 35:  # 近战范围
                player.take_damage(self.damage)
                self.attack_cooldown = 30  # 攻击间隔
                return True
        return False

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))
        # 显示血量
        bar_width = 30
        hp_ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, RED, (self.x - 15, self.y - 20, bar_width, 4))
        pygame.draw.rect(screen, GREEN, (self.x - 15, self.y - 20, bar_width * hp_ratio, 4))

# ---------- 主游戏循环 ----------
def main():
    # 选择角色（通过修改这些预定义角色可以添加动漫人物）
    # 路飞：橡胶手枪（远程直线弹幕）
    luffy_skill = Skill("橡胶手枪", 35, 40, 90, 400, projectile_speed=10)
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, "路飞", ORANGE, 150, 15, luffy_skill)

    # 备选角色定义（注释掉，可自行替换）
    # 鸣人：影分身·螺旋连击（近战大范围AOE）
    # naruto_skill = Skill("影分身连击", 60, 60, 120, 80, aoe_radius=80)
    # player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, "鸣人", YELLOW, 180, 20, naruto_skill)
    
    # 悟空：龟派气功（穿透性光束）
    # goku_skill = Skill("龟派气功", 50, 70, 150, 500, projectile_speed=12)
    # player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, "悟空", BLUE, 200, 18, goku_skill)

    enemies = []
    projectiles = []
    score = 0
    font = pygame.font.SysFont("Arial", 20)

    # 生成敌人波次
    spawn_timer = 0
    running = True
    while running:
        dt = clock.tick(FPS)
        screen.fill(BLACK)

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:  # 普通攻击
                    if player.attack_timer == 0:
                        # 近战攻击：检测前方敌人
                        atk_range = 50
                        for enemy in enemies:
                            if enemy.alive:
                                dx = enemy.x - player.x
                                dy = enemy.y - player.y
                                dist = math.hypot(dx, dy)
                                # 攻击判定在玩家前方一个扇形区域
                                if dist < atk_range and (dx * player.facing) > 0:
                                    enemy.take_damage(player.atk_damage)
                                    # 击退效果
                                    enemy.x += player.facing * 20
                                    break
                        player.attack_timer = 20  # 攻击硬直

                elif event.key == pygame.K_k:  # 必杀技
                    if player.use_skill():
                        skill = player.skill
                        if skill.projectile_speed > 0:  # 远程弹幕
                            direction = (player.facing, 0)
                            proj = Projectile(player.x, player.y, direction, skill.damage, skill.projectile_speed, YELLOW)
                            projectiles.append(proj)
                        elif skill.aoe_radius > 0:  # 范围爆发
                            # 直接伤害周围敌人
                            for enemy in enemies:
                                if enemy.alive:
                                    dist = math.hypot(enemy.x - player.x, enemy.y - player.y)
                                    if dist < skill.aoe_radius:
                                        enemy.take_damage(skill.damage)
                            # 绘制范围特效（短暂闪光）
                            pygame.draw.circle(screen, WHITE, (int(player.x), int(player.y)), skill.aoe_radius, 2)

        # 玩家移动
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = 1
        player.move(dx, dy)

        # 更新玩家
        player.update()

        # 更新弹幕
        for proj in projectiles[:]:
            if not proj.update():
                projectiles.remove(proj)
                continue
            # 检测弹幕与敌人碰撞
            for enemy in enemies:
                if enemy.alive:
                    dist = math.hypot(proj.x - enemy.x, proj.y - enemy.y)
                    if dist < proj.radius + enemy.width/2:
                        enemy.take_damage(proj.damage)
                        projectiles.remove(proj)
                        break

        # 敌人AI
        for enemy in enemies[:]:
            if enemy.alive:
                enemy.move_towards(player.x, player.y)
                enemy.update()
                enemy.attack_player(player)
                enemy.draw(screen)
            else:
                enemies.remove(enemy)
                score += 10

        # 玩家存活检测
        if not player.alive:
            game_over_text = font.render("GAME OVER - Press R to Restart", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
            if keys[pygame.K_r]:
                main()  # 重新开始
                return
            pygame.display.flip()
            continue

        # 生成敌人
        spawn_timer += 1
        if spawn_timer > 60 and len(enemies) < 5:
            side = random.choice(["left", "right", "top", "bottom"])
            if side == "left":
                ex, ey = 0, random.randint(50, SCREEN_HEIGHT-50)
            elif side == "right":
                ex, ey = SCREEN_WIDTH, random.randint(50, SCREEN_HEIGHT-50)
            elif side == "top":
                ex, ey = random.randint(50, SCREEN_WIDTH-50), 0
            else:
                ex, ey = random.randint(50, SCREEN_WIDTH-50), SCREEN_HEIGHT
            enemies.append(Enemy(ex, ey, hp=60, damage=12, speed=1.5, color=RED))
            spawn_timer = 0

        # 绘制所有对象
        for proj in projectiles:
            proj.draw(screen)
        player.draw(screen)

        # UI文本
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        skill_text = font.render(f"Skill: {player.skill.name} (CD:{player.skill.current_cooldown})", True, WHITE)
        screen.blit(skill_text, (10, 40))
        control_text = font.render("WASD:Move | J:Attack | K:Skill", True, WHITE)
        screen.blit(control_text, (10, 70))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()