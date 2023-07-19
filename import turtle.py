import turtle

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("white")

    # Turtle oluşturma
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("pink")
    t.speed(1)  # Çizim hızı (1 en yavaş, 10 en hızlı)

    # Üçgen çizimi
    for _ in range(3):
        t.forward(100)  # İleri git 100 birim
        t.left(120)     # 120 derece sola dön

    # Pencereyi kapatmak için tıklayana kadar bekle
    window.exitonclick()

draw_triangle()








