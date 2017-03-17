def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100

# 이 함수는 다른 곳에서 import해서 어디든지 사용할수 있다

if __name__ == "__main__":
    print(calculate_price_with_vat(100, 20))
