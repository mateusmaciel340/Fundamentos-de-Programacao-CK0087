"""
Exercício 13: Conversão de tempo

Um vídeo tem `98765` segundos de duração. Converta esse valor para horas, minutos e segundos, usando `//` e `%`.

Exemplo: `3661` segundos = 1 hora, 1 minuto e 1 segundo.

Seu código deve funcionar para qualquer inteiro `total_segundos`. Teste trocando `98765` por `3661`.
"""

duracao_video_segundos = 98765

"""
horas   | minutos  | segundos | 
27.43.. | 1646,..  | 98765s   |

horas = 98765 / 3600 => 27.43..., 98765 // 3600 = 27
minutos = 98765 % 3600 => 98765 = 3600 * 27 + r => r = 98765 - 97200 => r = 1565s
        = 1565 // 60 = 26
        
segundos = 1565 % 60 => 1565 = 60 * 26 + r => r = 1565 - 1560 = 5

horas: (27 * 3600) + minutos: (26 * 60) + segundos(5) => 97200 + 1560 + 5 => 98765
"""

horas = duracao_video_segundos // 3600
minutos = (duracao_video_segundos % 3600) // 60
segundos = (duracao_video_segundos % 3600) % 60

print(f"{horas}h{minutos}min{segundos}s")