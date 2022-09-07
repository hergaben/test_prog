class main():
    def __init__(self):
        self.status = "A"

    def split(self):
        match self.status:
            case "A":
                self.status = "B"
                return 0
            case "C":
                self.status = "F"
                return 4
            case "D":
                self.status = "E"
                return 5
            case "E":
                self.status = "F"
                return 6
            case _:
                raise KeyError

    def skid(self):
        match self.status:
            case "B":
                self.status = "C"
                return 2
            case "C":
                self.status = "D"
                return 3
            case "E":
                self.status = "A"
                return 8
            case _:
                raise KeyError

    def join(self):
        match self.status:
            case "E":
                self.status = "C"
                return 7
            case "A":
                self.status = "F"
                return 1
            case _:
                raise KeyError



# from enum import Enum
#
#
# class State(Enum):
#     A = 0
#     B = 1
#     C = 2
#     D = 3
#     E = 4
#     F = 5
#
#
# class StateMachine:
#     def __init__(self):
#         self.status = "A"
#
#     def split(self):
#         return self.update({
#             State.A: [State.B, 0],
#             State.C: [State.F, 4],
#             State.D: [State.E, 5],
#             State.E: [State.F, 6],
#         })
#
#     def join(self):
#         return self.update({
#             State.A: [State.F, 1],
#             State.E: [State.C, 7],
#         })
#
#     def skid(self):
#         return self.update({
#             State.B: [State.C, 2],
#             State.C: [State.D, 3],
#             State.E: [State.A, 8],
#         })
#
#     def update(self, transitions):
#         self.state, signal = transitions[self.state]
#         return signal
#
# if __name__ == '__main__':
#     x = StateMachine('split', 'skid', 'skid', 'split', 'join', 'skid', 'split', 'skid', 'join')
#     print(x())