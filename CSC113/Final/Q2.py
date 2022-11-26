#	Name: Mohamed Kharma
#	Final Exam

# ========================================================================
# Question 2
print('|Question 2|')
class SchedulerSPM():
    def __init__(self):
        pass
    def __str__(self):
        pass
    def Configure(self):
        pass

class SchedulerAedesAegypti(SchedulerSPM):
    def __init__(self,makeDecision=AedesAegypti(),executeDecision=AedesAegypti()):
        self.makeDecision=makeDecision
        self.executeDecision=executeDecision

class AedesAegypti():
    def __init__(self,lifeStage,energyLevel):
        self.lifeStage = lifeStage
        self.energyLevel = energyLevel
    def __str__(self):
        return "{}, {}".format(self.lifeStage,self.energyLevel)
    def Birth(self):
        pass
    def Metamorphosis(self):
        pass
    def Death(self):
        pass
    def FlyingRandomly(self):
        pass
    def LookForRestingPlace(self):
        pass
    def LookForPlant(self):
        pass
    def Feeding(self):
        pass
    def Mating(self):
        pass
    def Oviposting(self):
        pass

class SchedulerMammal(SchedulerSPM):
    def __init__(self,executeBehaviour=Mammal()):
        self.executeBehaviour=executeBehaviour

class Mammal():
    def __init__(self,traceIntensity):
        self.traceIntensity = traceIntensity
    def __str__(self):
        return "{}".format(self.traceIntensity)
    def MovingRandomly(self):
        pass
    def UpdateTrace(self):
        pass

class SchedulerVegetation(SchedulerSPM):
    def __init__(self,updateTrace=Vegetation()):
        self.updateTrace=updateTrace

class Vegetation():
    def __init__(self,trace_intensity):
        self.trace_intensity = trace_intensity
    def __str__(self):
        return "{}".format(self.trace_intensity)
    def UpdateTrace(self):
        pass

class SchedulerContainer(SchedulerSPM):
    def __init__(self,updateLiquidLevel=Container(),updateTrace=Container()):
        self.updateLiquidLevel=updateLiquidLevel
        self.updateTrace=updateTrace

class Container():
    def __init__(self,percentageLiquid,volatilityLiquid,percantageExposure,traceIntensity):
        self.percentageLiquid = percentageLiquid
        self.volatilityLiquid = volatilityLiquid
        self.percantageExposure = percantageExposure
        self.traceIntensity = traceIntensity
    def __str__(self):
        return "{},{},{},{}".format(self.percentageLiquid,self.volatilityLiquid,self.percantageExposure,self.traceIntensity)
    def updateVolume(self):
        pass
    def UpdateTrace(self):
        pass

class SchedulerMeteorology(SchedulerSPM):
    def __init__(self,updateEnvironment=Meteorology()):
        self.updateEnvironment=updateEnvironment

class Meteorology():
    def __init__(self, windDirection, windDirectionSpeed, accumRainfall, \
                 accumSolarRadiation, globalSolarRadiation, airTemp, \
                 highAirTemp, lowAirTemp, airRelativeHumidity, \
                 windSpeed, highWindSpeed):
        self.windDirection=windDirection
        self.windDirectionSpeed=windDirectionSpeed
        self.accumRainfall=accumRainfall
        self.accumSolarRadiation=accumSolarRadiation
        self.globalSolarRadiation=globalSolarRadiation
        self.airTemp=airTemp
        self.highAirTemp=highAirTemp
        self.lowAirTemp=lowAirTemp
        self.airRelativeHumidity=airRelativeHumidity
        self.windSpeed=windSpeed
        self.highWindSpeed=highWindSpeed
    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}".format(self.windDirection,self.windDirectionSpeed,self.accumRainfall,\
                                                         self.accumSolarRadiation,self.globalSolarRadiation,self.airTemp,\
                                                         self.highAirTemp,self.lowAirTemp,self.airRelativeHumidity,\
                                                         self.windSpeed,self.highWindSpeed)
    def updateData(self):
        pass
# ========================================================================
