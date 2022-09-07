def main(n):
    if n == 0:
        return -0.02
    if n >= 1:
        return (main(n-1)**3-96*main(n-1))/88
