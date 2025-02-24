import flet as ft
from conexao_pg import conn

class consulta_bd:
    def __init__(self,sql:str,valores:tuple):
        self.sql = sql
        self.valores = valores
        cursor = conn.cursor()
        cursor.execute(
            self.sql,self.valores
            
            )
        conn.commit()
class porcao(ft.UserControl):
    def __init__(self,nome,preco):
        super().__init__()
        self.nome = nome
        self.preco = preco
        
    def build(self):
        return ft.Container(
            padding=10,
            alignment=ft.alignment.top_center,
            shadow=ft.BoxShadow(blur_radius=15,color=ft.colors.WHITE12),
            content= ft.Text(
                   spans=[
                       ft.TextSpan(text=self.nome,style=ft.TextStyle(color=ft.colors.WHITE,weight=ft.FontWeight.BOLD)),
                        ft.TextSpan(text=f'    R$  {self.preco} ',style=ft.TextStyle(color=ft.colors.LIGHT_GREEN_ACCENT_400,weight=ft.FontWeight.BOLD))
                   ]
               )
        )

class pedido(ft.UserControl):
    def __init__(self,nome):
        super().__init__()
        self.nome = nome
    def build(self):
        return ft.Container(
            content= ft.Row(
                    spacing=0,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.icons.ARROW_RIGHT_ROUNDED,
                                icon_color=ft.colors.YELLOW,
                                height=20,
                                icon_size=40                            
                            ),
                            col=1,
                            offset=ft.Offset(x=0.0,y=-1.0)
                            ),
                        ft.Text(
                            value= self.nome.upper(),
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.YELLOW,
                            size=30,
                            col=5
                        ),
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.icons.ARROW_LEFT_ROUNDED,
                                icon_color=ft.colors.YELLOW,
                                height=20,  
                                icon_size=40                          
                            ),
                            offset=ft.Offset(x=0.0,y=-1.0)
                            )
                    ]
                )
        )

class lanche(ft.UserControl):
    def __init__(self,nome,receita,preco):
        super().__init__()
        self.nome = nome
        self.receita = receita
        self.preco = preco
    def build(self):
        return ft.Container(
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.WHITE12),
        alignment=ft.alignment.top_center,
        padding=10,
        content=ft.Column(
            controls=[
                ft.ResponsiveRow(
                    col=12,
                    spacing=0,
                    controls=[
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.icons.ARROW_RIGHT_ROUNDED,
                                icon_color=ft.colors.YELLOW,
                                height=20                            
                            ),
                            col=1,
                            offset=ft.Offset(x=0.0,y=-0.5)
                            ),
                        ft.Text(
                            value= self.nome.upper(),
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.YELLOW,
                            col=5
                        ),
                        ft.Text(
                                value=f'R$ {self.preco}',
                            col=3,
                            color=ft.colors.LIGHT_GREEN_ACCENT_400,
                            weight=ft.FontWeight.W_700
                        )
                    ]
                ),
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=10),
                    content=ft.Text(
                    value=self.receita,
                    color=ft.colors.WHITE,
                    
                )
                )
            ],
            
        )
    )
        