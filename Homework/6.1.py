import time
class TrafficLight:
    __color = ['red', 'yellow', 'green']
    def running(self):
        a = 10
        print(TrafficLight.__color[0])
        time.sleep(7)
        while True:
            print(TrafficLight.__color[1])
            time.sleep(2)
            print(TrafficLight.__color[2])
            time.sleep(10)
            print(TrafficLight.__color[0])
            time.sleep(10)

trafficlight_1 = TrafficLight()
trafficlight_1.running()
