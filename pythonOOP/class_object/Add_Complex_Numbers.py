class Add_Complex_Numbers:
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag

    def add(self, number):
        result_real = self.real + number.real
        result_imaginary = self.imaginary + number.imaginary

        # create another object on complex
        result = Add_Complex_Numbers(result_real, result_imaginary)
        return result


n1 = Add_Complex_Numbers(5, 6)
n2 = Add_Complex_Numbers(-4, 2)

n3 = n1.add(n2)
print('real part ', n3.real)
print(f'Imaginary {n3.imaginary}')