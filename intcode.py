import unittest
from unittest.mock import patch
from lib import get_input


class Intcode(object):
    """
    Opcode descriptions:
    Opcode 1 adds together numbers read from two positions and stores the result in a third position
    Opcode 2 multiplies together numbers read from two positions and stores the result in a third position
    Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
    Opcode 4 outputs the value of its only parameter
    Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter.
      Otherwise, it does nothing.
    Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter.
      Otherwise, it does nothing.
    Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
      Otherwise, it stores 0.
    Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
      Otherwise, it stores 0.

    Parameter Modes:
      0 - Position mode
      1 - Immediate mode
    """
    params_per_code = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        99: 0
    }

    def __init__(self, day=2, _input=None, use_phase_settings=False, phase_setting=0, input_signal=0, amp_loop=False, print_output=False):
        self.instruction_pointer = 0
        self.input = get_input(day) if not _input else _input
        self.diagnostic_codes = []
        self.use_phase_settings = use_phase_settings
        self.phase_setting = phase_setting
        self.input_signal = input_signal
        self.first_input = True
        self.print_output = print_output
        self.amp_loop = amp_loop

    def run(self):
        out = self.step()
        while(out is not True):
            out = self.step()

    def step(self):
        # Parse Opcode and paramater modes, get instruction
        op_code = str(self.input[self.instruction_pointer])
        if len(op_code) > 2:
            x = op_code
            op_code = int(x[-2:])  # last two digits
            param_modes = [int(p) for p in(
                x[:-2][::-1] + '0' * (self.params_per_code[op_code] - len(x[:-2])))]
        else:
            op_code = int(op_code)
            param_modes = [0 for param in range(self.params_per_code[op_code])]

        instruction = self.input[self.instruction_pointer:
                                 self.instruction_pointer + 1 + self.params_per_code[op_code]]
        auto_increment_pointer = True

        # Follow instruction
        if op_code == 1:
            a = self.input[instruction[1]
                           ] if param_modes[0] == 0 else instruction[1]
            b = self.input[instruction[2]
                           ] if param_modes[1] == 0 else instruction[2]
            self.input[instruction[3]] = a + b
        elif op_code == 2:
            a = self.input[instruction[1]
                           ] if param_modes[0] == 0 else instruction[1]
            b = self.input[instruction[2]
                           ] if param_modes[1] == 0 else instruction[2]
            self.input[instruction[3]] = a * b
        elif op_code == 3:
          if self.use_phase_settings:
            if self.first_input:
              # use phase setting
              self.input[instruction[1]] = self.phase_setting
              self.first_input = False
            else:
              # use input signal
              self.input[instruction[1]] = self.input_signal
          else:
            single_int_input = int(input("Input a single integer:\n>"))
            self.input[instruction[1]] = single_int_input
        elif op_code == 4:
            diag_code = self.input[instruction[1]] if int(
                param_modes[0]) == 0 else instruction[1]
            self.diagnostic_codes.append(diag_code)
            if self.amp_loop:
              self.input_signal = diag_code
            if self.print_output:
              print("Output: {}".format(diag_code))
        elif op_code == 5:
            param = self.input[instruction[1]
                               ] if param_modes[0] == 0 else instruction[1]
            if param != 0:
                auto_increment_pointer = False
                self.instruction_pointer = self.input[instruction[2]
                                                      ] if param_modes[1] == 0 else instruction[2]
        elif op_code == 6:
            param = self.input[instruction[1]
                               ] if param_modes[0] == 0 else instruction[1]
            if param == 0:
                auto_increment_pointer = False
                self.instruction_pointer = self.input[instruction[2]
                                                      ] if param_modes[1] == 0 else instruction[2]
        elif op_code == 7:
            a = self.input[instruction[1]
                           ] if param_modes[0] == 0 else instruction[1]
            b = self.input[instruction[2]
                           ] if param_modes[1] == 0 else instruction[2]
            if a < b:
                self.input[instruction[3]] = 1
            else:
                self.input[instruction[3]] = 0
        elif op_code == 8:
            a = self.input[instruction[1]
                           ] if param_modes[0] == 0 else instruction[1]
            b = self.input[instruction[2]
                           ] if param_modes[1] == 0 else instruction[2]
            if a == b:
                self.input[instruction[3]] = 1
            else:
                self.input[instruction[3]] = 0
        elif op_code == 99:
            if self.print_output:
              print("Program halting!")
            return True
        else:
            print("Unknown opcode: {}".format(op_code))
            return True

        # increment instruction pointer if applicable
        if auto_increment_pointer:
            self.instruction_pointer += 1 + self.params_per_code[op_code]


class IntcodeTest(unittest.TestCase):
    def test_day2_example1(self):
        i = Intcode(_input=[1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        i.run()
        self.assertEqual(i.input[0], 3500)

    def test_day2_example2(self):
        i = Intcode(_input=[1, 0, 0, 0, 99])
        i.run()
        self.assertEqual(i.input, [2, 0, 0, 0, 99])

    def test_day2_example3(self):
        i = Intcode(_input=[2, 3, 0, 3, 99])
        i.run()
        self.assertEqual(i.input, [2, 3, 0, 6, 99])

    def test_day2_example4(self):
        i = Intcode(_input=[2, 4, 4, 5, 99, 0])
        i.run()
        self.assertEqual(i.input, [2, 4, 4, 5, 99, 9801])

    def test_day2_example5(self):
        i = Intcode(_input=[1, 1, 1, 4, 99, 5, 6, 0, 99])
        i.run()
        self.assertEqual(i.input, [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_day2_part1(self):
        i = Intcode(day=2)
        i.input[1] = 12
        i.input[2] = 2
        i.run()
        self.assertEqual(i.input[0], 9581917)

    @patch('builtins.input', return_value='1')
    def test_day5_part1(self, input):
        i = Intcode(day=5)
        i.run()
        self.assertEqual(list(set(i.diagnostic_codes)), [0, 9654885])

    @patch('builtins.input', return_value='7')
    def test_day5_large_example_le_8(self, input):
      i = Intcode(_input=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
      i.run()
      self.assertEqual(i.diagnostic_codes, [999])


    @patch('builtins.input', return_value='8')
    def test_day5_large_example_eq_8(self, input):
      i = Intcode(_input=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
      i.run()
      self.assertEqual(i.diagnostic_codes, [1000])

    @patch('builtins.input', return_value='9')
    def test_day5_large_example_gt_8(self, input):
      i = Intcode(_input=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
      i.run()
      self.assertEqual(i.diagnostic_codes, [1001])


if __name__ == "__main__":
    unittest.main()
