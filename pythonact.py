def float_Point(Real_num):
        value = 0
        if(Real_num < 0):
                value = 1
        Real_num = abs(Real_num)
        intit_str = bin(int(Real_num))[2 : ]
        binary = ''
        answer=Real_num - int(Real_num)
        while (answer):
                answer *= 2
                if (answer >= 1):
                        Given_first_sec = 1
                        answer -= 1
                else:
                        Given_first_sec = 0
                binary += str(Given_first_sec)

        sol = intit_str.index('1')
        expon_str = bin((len(intit_str) - sol - 1) + 127)[2 : ]
        m_str = intit_str[sol + 1 : ] + binary
        m_str =         m_str + ('0' * (23 - len(       m_str)))
        return (str(value) + '|' + expon_str + '|' + m_str)

float_Point(float(input()))
