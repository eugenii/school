data = [262, 231, 341, 250, 236, 254, 210, 279, 268, 289, 344, 290, 394, 332, 296, 302, 312, 328, 378, 237, 302, 245, 368, 241, 271, 322, 219, 341, 242, 229, 244, 395, 315, 220, 353, 241, 233, 204, 261, 275, 230, 353, 202, 390, 399, 349, 294, 309, 342, 380, 225, 336, 264, 259, 342, 333, 327, 359, 216, 246, 362, 261, 214, 313, 353, 260, 318, 283, 342, 210, 364, 379, 310, 341, 362, 384, 362, 338, 382, 386, 329, 374, 224, 215, 214, 346, 337, 250, 307, 309, 217, 377, 332, 385, 310, 251, 249, 228, 374, 251, 221, 309, 209, 357, 256, 222, 215, 367, 313, 288, 205, 338, 308, 344, 213, 392, 333, 330, 381, 327, 326, 399, 338, 203, 208, 268, 286, 350, 314, 219, 251, 317, 306, 387, 336, 340, 310, 231, 326, 317, 205, 276, 243, 262, 265, 366, 282, 241, 219, 389, 328, 254, 207, 256, 343, 341, 241, 266, 371, 276, 358, 201, 342, 207, 356, 213, 329, 368, 268, 367, 201, 235, 399, 393, 209, 364, 377, 363, 284, 329, 213, 309, 278, 391, 272, 392, 208, 291, 285, 273, 250, 376, 221, 295, 336, 308, 309, 205, 213, 209, 272, 229, 331, 316, 273, 253, 262, 361, 216, 342, 255, 383, 299, 268, 237, 363, 224, 202, 213, 251, 387, 212, 350, 320, 364, 216, 205, 320, 200, 346, 246, 290, 263, 257, 220, 328, 297, 295, 314, 242, 292, 212, 315, 214, 389, 237, 270, 258, 342, 226, 236, 253, 325, 338, 246, 394, 362, 205, 315, 321, 347, 259, 377, 396, 390, 374, 205, 243, 225, 375, 206, 242, 372, 275, 253, 201, 270, 254, 395, 332, 367, 281, 217, 223, 290, 361, 351, 283, 297, 321, 261, 387, 369, 249, 240, 262, 296, 286, 359, 203]
t1 = 1  # evens
t1_t = 1
t2 = 1  # % 3 == 0
t2_t = 1
t3 = 1  # delta <= 5
t3_t = 1

for i in range(len(data) - 1):
    if data[i + 1] % 2 == 0 and data[i] % 2 == 0:
        t1_t += 1
    else:
        if t1 < t1_t:
            t1 = t1_t
            index1 = i
            print(data[i - t1 - 1: i + 2])
        t1_t = 1
    if data[i + 1] % 3 == 0 and data[i] % 3 == 0:
        t2_t += 1
    else:
        if t2 < t2_t:
            t2 = t2_t
        t2_t = 1
    if abs(data[i + 1] - data[i]) <= 5:
        t3_t += 1
    else:
        if t3 < t3_t:
            t3 = t3_t
            index3 = i
            print(data[i - t3 - 1: i + 1])
        t3_t = 1
        
print(t1, t2, t3)