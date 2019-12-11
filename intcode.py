from lib import get_input


class Intcode(object):
    params_per_code = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        99: 0
    }

    def __init__(self, day=2):
        self.instruction_pointer = 0
        self.input = get_input(day)
        self.input = [1101, 100, -1, 4, 0]

    def step(self):
        op_code = str(self.input[self.instruction_pointer])
        if len(op_code) > 2:
            x = op_code
            op_code = int(x[-2:])  # last two digits
            param_modes = [int(p) for p in(
                x[:-2][::-1] + '0' * (self.params_per_code[op_code] - len(x[:-2])))]
        else:
            op_code = int(op_code)
            param_modes = '0' * self.params_per_code[op_code]
        instruction = self.input[self.instruction_pointer:
                                 self.instruction_pointer + 1 + self.params_per_code[op_code]]
        print(instruction, op_code, param_modes)
        if op_code == 1:
            pass
        elif op_code == 2:
            pass
        elif op_code == 3:
            pass
        elif op_code == 4:
            pass
        elif op_code == 99:
            pass


if __name__ == "__main__":
    i = Intcode(day=5)
    i.step()
