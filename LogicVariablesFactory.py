class LogicVariables:
    class LogicVersion:
        def IsProd():
            return False
        def IsDev():
            return True
        def IsStage():
            return False
        def IsDeveloperBuild():
            return True
        