def can_square_contain(N, W, H):
    start = 1
    if W > H:
        end = W * N
    else:
        end = H * N

    while start < end:
        mid = (start + end) // 2

        if N <= (mid // H) * (mid // W):
            end = mid
        elif N > (mid // H) * (mid // W):
            start = mid + 1

    return start
