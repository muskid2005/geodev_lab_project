# with open("wards.csv") as f:
#     lines = f.readlines()

# for line in lines[1:]:
#     parts = line.strip().split(",")
#     ward = parts[0]
#     area_km2 = float(parts[1])
#     if area_km2 > 9:
#         print(f"{ward} is large")
#     else:
#         print(f"{ward} is small")

with open("wards.csv") as f:
    lines = f.readlines()

def main(ward, size):
    return(f"{ward} is {size}")


for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    size = "unknown"
    if area_km2 < 9:
        size = "small"
    else:
        size = "large"
    if __name__ == "__main__":
        print(main(ward, size))


