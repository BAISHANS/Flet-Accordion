import flet as ft
import os 

cwd = os.getcwd()

class ChildCard(ft.Container):
    
    def __init__(self,bgcolor,width,height):
        # 动画函数
        def _on_hover(e):
            # 改变
            
            if not e.control.data:
                self.height += 50
                self.width += 25
                e.control.data = 1
                
            # 还原
            else:
                self.height -= 50
                self.width -= 25
                e.control.data = 0
            self.update()



        super().__init__(
            bgcolor=ft.colors.with_opacity(opacity=0.2,color=bgcolor),
            width=width,
            height=height,
            blur=ft.Blur(sigma_x=15,sigma_y=15,tile_mode=ft.BlurTileMode.MIRROR),
            border_radius=12,
            on_hover=_on_hover,
            animate=ft.Animation(duration=1500,curve=ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN)
        )


class MainContainer(ft.Container):
    def __init__(self, ):
        _row = ft.Row(
            [ChildCard(bgcolor=ft.colors.WHITE,width=80,height=500) for _ in range(8)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        
        super().__init__(
            blur=ft.Blur(sigma_x=15,sigma_y=15,tile_mode=ft.BlurTileMode.MIRROR),
            content=_row,
            alignment=ft.Alignment(0,0),
            expand=True,
            

        )


def main(page:ft.Page):
    page.bgcolor = ft.colors.GREY_500
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    maincard = MainContainer()
    
    img = ft.Image(src=r"C:\Users\Administrator\Desktop\PYGUI\flet\Main\手风琴\BACKGROUND.jpg",fit=ft.ImageFit.CONTAIN,)
    stack = ft.Stack(
        [img,
        maincard],
        expand=True)
        
    page.add(stack)
    page.update()

if __name__=='__main__':
    ft.app(main)