# --- Assets (Short Names) ---

# Characters
define k = Character("Ким", image="k")
define mom = Character("Мама")
define mon = Character("Моник")
define cop = Character("Коп") # это один перс для всех копов.
define path = Character("Патологоанатом")
define head = Character("Воспитатель")
define mrs_s = Character("Миссис Так-Себе")

define shadow = Character("???", color="#555555")
define weyd = Character("Вейд")
define avi = Character("Авиариус")
define shigo = Character("Шиго")
define go = Character("Миссис Го")
define daf = Character("Дафф Киллиган")
define drakk = Character("Драк Макак")

# Backgrounds
image bg office_full = "images/bg/bg_office_full.jpg" # Общий план
image bg office_home = "images/bg/bg_office_home.jpg" # Жилая зона
image bg office_worbench = "images/bg/bg_office_worbench.jpg" # Рабочая зона
image bg office_window = "images/bg/bg_office_window.jpg" # Окно и вид на город, под углом сверху вниз
#image bg car = "images/bg/car.jpg" универсальная сцена в машине
image bg warehouse = "images/bg/bg_warehouse.jpg" #склад - драк макак
image bg kindergarten = "images/bg/bg_kindergarten.jpg" # детский сад, общий план
image bg street = "images/bg/bg_street.jpg" # универсальная улица
image bg black = "images/bg/bg_black.jpg"

image bg library = "images/bg/bg_library.jpg"
image bg school = "images/bg/bg_school.jpg"
image bg prison = "images/bg/bg_prison.jpg"
image bg cafe = "images/bg/bg_cafe.jpg"
image bg port = "images/bg/bg_port.jpg"
image bg mountains = "images/bg/bg_mountains.jpg"
image bg castle = "images/bg/bg_castle.jpg"
image bg castle_hall = "images/bg/bg_castle_hall.jpg"
image bg cliff = "images/bg/bg_cliff.jpg"
image bg hospital = "images/bg/bg_hospital.jpg"
image bg park = "images/bg/bg_park.jpg"
image bg road = "images/bg/bg_road.jpg"
image bg white = "images/bg/bg_white.jpg"

#Анимация дыма - верхний слой

# особая сцена - мигающий свет, нарачито зацензурен драк макак
# Особая картинка ракурс снизу рыбий глаз, патологоанатом палец один глаз очень большой, как будто смотрит в душу
# фото из детского сада


# Sprites
image telephone = "images/sprites/telephone.png"

image k normal = "images/sprites/k_normal.png"
image k sad = "images/sprites/k_sad.png"
image k thinking = "images/sprites/k_thinking.png"
image k angry = "images/sprites/k_angry.png"
image mon happy = "images/sprites/mon_happy.png"
image mon worried = "images/sprites/mon_worried.png"
image weyd normal = "images/sprites/weyd_normal.png"
image cop tired = "images/sprites/cop_tired.png" 
image path normal = "images/sprites/path_normal.png"
image head normal = "images/sprites/head_normal.png"
image avi cell = "images/sprites/avi_cell.png"
image go normal = "images/sprites/go_normal.png"
image shigo teacher = "images/sprites/shigo_teacher.png"

# Audio
define audio.rain = "audio/audio_rain.ogg"
define audio.phone = "audio/audio_phone.ogg"
define audio.typewriter = "audio/audio_typewriter.ogg"
define audio.door = "audio/audio_door.ogg"
define audio.siren = "audio/audio_siren.ogg"

init offset = 0

# --- Game Start ---
label start:
    jump part1

# --- Game End ---
label end_of_game:
    return