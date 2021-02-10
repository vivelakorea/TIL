def maxProfit(self, prices: list[int]) -> int:

    # profit 없을 경우 0으로 리턴되어야 하므로 0으로 초기화
    profit = 0
    # 배열 내의 값들과 비교 후 최솟값을 저장하는 변수: 최대로 초기화해야 비교했을때 무조건 떨어짐
    min_price = sys.maxsize

    for i in prices:
        min_price = min(min_price, i)
        profit = max(profit, i - min_price)

    return profit
