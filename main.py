import HikingLog
import demo


def main():
    hikingLog = HikingLog.HikingLog().get()
    dem = demo.Demo(hikingLog)
    dem.startDemo()

main()