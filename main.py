from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina import *
app = Ursina()

tap = Audio(sound_file_name='tap.mp3', autoplay=False, pitch=1)
jump = Audio(sound_file_name='jump.mp3', autoplay=False, pitch=1)
Audio('music.mp3', autoplay=True)


def add():
    player.jump_height = 4

def gift():
    WindowPanel(
        title='Story line',
        content=(
            Text('''
            The villagers have sent you a gift
            Jump boost and long view
            '''),
        ),
        popup=True,
        enabled=True
    )
    camera.fov = -40
    player.jump_height = 5
    player.jump_duration = 5

def Win():
    WindowPanel(
        title='Story line',
        content=(
            Text('''
                You won.
                '''),
        ),
        popup=True,
        enabled=True
    )
    window.exit_button.on_click = application.quit

bg = Entity(model='quad', scale=(50,12), texture='bg')
bg2 = Entity(model='quad', scale=(50,12), texture='bg2', position=(50, 0))

des_ground = Entity(model='cube', scale=(25, 1), y=-4, x=-15, collider='box', color=color.brown)
Entity(model='cube', texture='white_cube', position = (0, -4), collider='box', color=color.green)
Entity(model='cube', texture='white_cube', position = (4, -4), collider='box', scale=(.3, 1), color=color.green)
Entity(model='cube', texture='white_cube', position = (7, -1), collider='box', scale=(1, 1), color=color.green)
Entity(model='cube', texture='white_cube', position = (7, 2), collider='box', scale=(1, 1), color=color.green)
Entity(model='cube', texture='white_cube', position = (9, -4), collider='box', scale=(3, 1), color=color.green)
Entity(model='cube', texture='white_cube', position = (50, -4), collider='box', scale=(25, 1), color=color.green)

EditorCamera()

player = PlatformerController2d(jump_height=3, y=2, x=-23, always_on_top=True, texture='player.png')
camera.add_script(SmoothFollow(target=player, offset=[0,4,-30], speed=4))

Button(model='cube', text='<red>Looks like he has made some traps for his safty', parent=scene, y=1)
Button(model='cube', text='<red>No terrain, you need to find another path', parent=scene, y=-4, x=17)
Button(model='cube', text='<red>You found the troll path', parent=scene, y=0, x=21).on_click = add
Button(model='cube', parent=scene, text='<red>Massage', y=3, x=29).on_click = gift
Button(model='cube', parent=scene, y=3, x=21)
Button(model='cube', parent=scene, y=-3, x=-25.5, text='rage quit').on_click = application.quit

start_text = WindowPanel(
    title='Story line',
    content=(
        Text('''
        A <red>evil fire lord<default> has <red>corrupted<default> the medeval time period
        And It's your work to defeat him
        For that you have a invisiable sword
        You need to get close to him and <red>kill him<default>
        (Remember pressingd on close will make the game think you died)
        Tap to continue.
        '''),
        ),
        popup=True,
        enabled=True
    )

story2 = WindowPanel(
    title='<red>Evil Lord<red>',
    content=(
        Text('''
        <red>Evil: You thought that this is enough to kill me
        <default>You: What do you mean?
        <red>Evil: Our souls are interconnected. If you attack me then you will attack yourself.
        <default>You: So, I get attacked then you will be the one to feel the pain.
        <red>Evil: Yea, nothing in this world will attack you. Neither the villager nor my soldier.
        <default>You: I can jump off and die.
        <red>Evil: That will teleport you, you won't take a damage.
        <default>You: So you are immortal.
        <red>Evil: Yes
        <default>You: there has to be a way
        (<yellow>You sword broke<default>)
        Tap to continue.
        '''),
        ),
        popup=True,
        enabled=False
    )

evil = Entity(model='cube',collider='box', scale_y=2, position=(60, -2), texture='evil.png')
ab = 1
def update():
    if player.position.y < -9:
        player.position = (-23, 2)
    a = 1
    if player.x > 58 and player.y < -3 and a == 1:
        story2.enabled = True
        window.exit_button.enabled = True
        a = 2

window.exit_button.enabled = False
window.exit_button.on_click = Win

def input(key):
    if key == 'left mouse down':
        tap.play()
    if key == 'space':
        jump.play()

app.run()