from currency_service.exceptions import NotFound


class ProductNotFound(NotFound):
    error_code = 'product_not_found'

    def __init__(self, sku, seller):
        self.error_message = (
            f'Product with sku {sku} and seller {seller} was not found'
        )
