import tools
def main(): #區域變數
    height:int = int(input("請輸入身高公分"))
    weight:int = int(input("請輸入體重公斤"))
    BMI:float = tools.get_bmi(weight,height)

    print(f"身高:{height}""cm")
    print(f"體重:{weight}""kg")
    print(f"BMI:{BMI}")
    status:str = tools.get_status(BMI)   
    print(f"狀態為:{status}")

if __name__ == '__main__':
    main()   #全域變數