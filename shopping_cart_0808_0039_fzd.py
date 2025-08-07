# 代码生成时间: 2025-08-08 00:39:42
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import uuid

# 定义购物车类
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        """添加商品到购物车"""
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity

    def remove_item(self, item):
        """从购物车移除商品"""
        if item in self.cart:
            del self.cart[item]

    def update_item(self, item, quantity):
        """更新购物车中商品的数量"""
        if item in self.cart:
            self.cart[item] = quantity
        else:
            raise ValueError("商品不存在于购物车中")

    def get_cart(self):
        """获取购物车中的商品列表"""
        return self.cart

# 初始化Dash应用
def serve_layout():
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1("购物车示例"),
        html.Div(id="cart"),  # 展示购物车中的商品
        html.Button("添加商品", id="add-item", n_clicks=0),
        dcc.Input(id="item-name", type="text", placeholder="商品名称"),
        dcc.Input(id="item-quantity", type="number", placeholder="数量"),
        html.Button("更新购物车", id="update-cart", n_clicks=0),
        html.Button("清空购物车", id="clear-cart", n_clicks=0),
    ])

    # 回调函数：添加商品到购物车
def add_item_to_cart(n_clicks, item_name, item_quantity):
    if n_clicks is None or item_name is None or item_quantity is None:
        raise PreventUpdate

    cart = ShoppingCart()
    cart.add_item(item_name, int(item_quantity))
    return cart.get_cart()

    # 回调函数：清空购物车
def clear_cart(n_clicks):
    if n_clicks is None:
        raise PreventUpdate

    cart = ShoppingCart()
    cart.clear_cart()
    return {}

    # 回调函数：更新购物车
def update_cart(n_clicks, item_name, new_quantity):
    if n_clicks is None or item_name is None or new_quantity is None:
        raise PreventUpdate

    cart = ShoppingCart()
    cart.update_item(item_name, int(new_quantity))
    return cart.get_cart()

    # 回调函数：展示购物车
def display_cart(cart):
    return html.Div([f"{item}: {quantity}" for item, quantity in cart.items()])

    app.callback(
        Output("cart", "children"),
        [Input("add-item", "n_clicks"), Input("update-cart", "n_clicks")],
        state=[State("item-name", "value"), State("item-quantity", "value")],
    )(input_func=add_item_to_cart)

    app.callback(
        Output("cart", "children"),
        [Input("clear-cart", "n_clicks")],
    )(input_func=clear_cart)

    app.callback(
        Output("cart", "children"),
        [Input("update-cart", "n_clicks")],
        state=[State("item-name", "value"), State("item-quantity", "value")],
    )(input_func=update_cart)

    return app.server

# 运行Dash应用
def main():
    server = serve_layout()
    if __name__ == "__main__":
        import os
        os.environ["DASH_DEBUG"] = "True"  # 开启Dash调试模式
        server.run(port=8050)

if __name__ == "__main__":
    main()