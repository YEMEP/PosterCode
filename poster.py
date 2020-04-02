import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as scp

V0 = 220 * (1/(3.24 * 10 ** (-17)))
def f(r,a):
    return ((V0**2 * a)/((r**2 + a**2)**(1/2)))**(1/2)
#Convert dataset
"""Vm = []
with open ("C:\\Users\\Paul YEME\\Desktop\\UBC Courses\\ASTR 403\\data.txt", 'r') as file:
    for line in file:
        l2 = line.split()
        Vm.append(float(l2[0]))
print(Vm)"""
np.vectorize(f)
vf =  np.array([ 113.13833, 183.93909, 205.94473, 209.5742, 213.65466, 217.76311, 220.42043, 220.9435, 219.61349, 217.20041, 214.48074, 211.99699, 210.16144, 209.05798, 208.42989, 208.05116, 207.94969, 208.18065, 208.68027, 209.34383, 210.20345, 211.27367, 212.42502, 213.57637, 214.75717, 216.01738, 217.34802, 218.69914, 220.0452, 221.38745, 222.71918, 224.02753, 225.29221, 226.48814, 227.59309, 228.59505, 229.49448, 230.29948, 231.01904, 231.66063, 232.23241, 232.74576, 233.21429, 233.65028, 234.06172, 234.45119, 234.81654, 235.15245, 235.45335, 235.71703, 235.94682, 236.15125, 236.34093, 236.52563, 236.71318, 236.91026, 237.12363, 237.3598, 237.6226, 237.91022, 238.21373, 238.51923, 238.81212, 239.08205, 239.32535, 239.54451, 239.7451, 239.93262, 240.11041, 240.27908, 240.43678, 240.58044, 
240.70805, 240.82172, 240.92969, 241.04605, 241.18678, 241.36386, 241.58003, 241.82735, 242.09055, 242.35335, 242.60484, 242.84296, 
243.07436, 243.3109, 243.56422, 243.84053, 244.13741, 244.44447, 244.7476, 245.0351, 245.30383, 245.56248, 245.83002, 246.12949, 246.47919, 246.88516, 247.33926, 247.82359, 248.3186, 248.81036, 249.29443, 249.77541, 250.26357, 250.76981, 251.30119, 251.85861, 252.43758, 253.03114, 253.63284, 254.23827, 254.84521, 255.45293, 256.06137, 256.67059, 257.28061, 257.89117, 258.50183, 259.11209, 259.72147, 260.32944, 260.93542, 261.53876, 262.13861, 262.73428, 263.32516, 263.91068, 264.49011, 265.06271, 265.62827, 266.18741, 266.74139, 267.29172, 267.83969, 268.38629, 268.9321, 269.4776, 270.02286, 270.56693, 271.10699, 271.63779, 272.15195, 272.64243, 273.10574, 273.54507, 273.97043, 274.39545, 274.83224, 275.28577, 275.75082, 276.21259, 276.65161, 277.05121, 277.4046, 277.71732, 278.0043, 278.28305, 278.56659, 278.85974, 279.15872, 279.45404, 279.73465, 279.99149, 280.21915, 280.41461, 280.57574, 280.70065, 280.78943, 280.84576, 280.87692, 280.89169, 280.89752, 280.89941, 280.89987, 280.89993, 280.89972, 280.8989, 280.89651, 280.89069, 280.87881, 280.85797, 280.82587, 280.78128, 280.72388, 280.65359, 280.57028, 280.47394, 280.36511, 280.24475, 280.11404, 279.97446, 279.8287, 279.68195, 279.54181, 279.41678, 279.31284, 279.23032, 279.1626, 279.09778, 279.02286, 278.92813, 278.80978, 278.66959, 278.51233, 
278.3432, 278.16614, 277.98383, 277.79813, 277.61057, 277.42245, 277.2352, 277.05057, 276.87112, 276.6998, 276.5394, 276.39182, 276.25809, 276.13898, 276.03491, 275.94522, 275.86655, 275.79178, 275.71109, 275.6152, 275.49942, 275.36646, 275.22656, 275.0943, 274.98334, 274.90158, 274.84924, 274.82053, 274.80722, 274.80209, 274.80048, 274.80008, 274.79999, 274.79999, 274.79999, 274.79999, 274.80002, 274.80023, 274.80115, 274.8045, 274.81393, 274.83582, 274.87833, 274.94861, 275.04858, 275.17224, 275.30603, 275.43274, 275.53763, 275.61301, 275.65961, 275.6842, 275.69553, 275.70163, 275.70929, 275.72543, 275.75748, 275.81238, 275.89343, 275.9975, 276.11429, 276.22928, 276.32855, 276.40338, 276.45224, 276.47955, 276.49219, 276.49582, 276.49271, 276.48087, 276.45471, 276.40741, 276.3342, 276.23615, 276.12158, 276.00415, 275.89801, 275.81229, 275.74707, 275.69327, 275.63602, 275.56052, 275.45731, 275.32477, 275.16782, 274.99463, 274.81287, 274.62857, 274.44632, 274.27039, 274.10486, 273.95297, 273.81598, 273.6929, 273.58105, 273.47693, 273.37625, 
273.27255, 273.15591, 273.01367, 272.83383, 272.61044, 272.34772, 272.05972, 271.76584, 271.48395, 271.22504, 270.99173, 270.7804, 270.58496, 270.39944, 270.21893, 270.03864, 269.85339, 269.65771, 269.44684, 269.21695, 268.96475, 268.68677, 268.3797, 268.04199, 267.67578, 267.2868, 266.88257, 266.47, 266.05414, 265.63837, 265.22513, 264.81659, 264.41443, 264.01959, 263.63202, 263.25101, 262.87543, 262.50333, 262.13089, 261.75146, 261.3562, 260.9364, 260.48752, 260.01257, 259.52225, 259.03192, 258.55627, 258.10458, 257.67896, 257.27597, 256.88971, 256.51465, 256.14667, 255.78258, 255.41977, 255.05626, 254.69177, 254.32901, 253.97456, 253.63809, 253.3293, 253.05351, 252.80794, 252.58128, 252.35722, 252.12041, 251.86205, 251.58263, 251.29083, 250.9994, 250.71992, 250.45914, 250.21806, 249.99365, 249.78151, 249.57787, 249.38008, 249.1864, 248.99551, 248.80679, 248.62097, 248.44098, 248.27267, 248.12408, 248.00316, 
247.91441, 247.85687, 247.82448, 247.80894, 247.8027, 247.80066, 247.80014, 247.80016, 247.80075, 247.80301, 247.80978, 247.82639, 247.86038, 247.91949, 248.00795, 248.12289, 248.25356, 248.38394, 248.4987, 248.58917, 248.65677, 248.71265, 248.77315, 248.85339, 248.96199, 249.09895, 249.25758, 249.42862, 249.60417, 249.77965, 249.95381, 250.12744, 250.30179, 250.47688, 250.65009, 250.81535, 250.9641, 251.08794, 251.18294, 251.25298, 251.30991, 251.3701, 251.44827, 251.55153, 251.67644, 251.81033, 251.93646, 252.04036, 252.11472, 252.16051, 252.18445, 252.19492, 252.19865, 252.19974, 252.19997, 252.2, 252.2, 252.2, 252.2, 252.19995, 252.19968, 252.19849, 252.1944, 252.18317, 252.15784, 252.11003, 252.03333, 251.92732, 251.80005, 251.66638, 251.54298, 251.44188, 251.36568, 251.30652, 251.24928, 251.17714, 251.07703, 250.94202, 250.77026, 250.56229, 250.31953, 250.04562, 249.74863, 249.44151, 249.13985, 248.8571, 
248.60069, 248.37085, 248.16254, 247.96878, 247.78273, 247.59756, 247.40514, 247.19569, 246.95998, 246.6937, 246.40182, 246.09973, 245.80965, 245.55286, 245.34135, 245.17294, 245.03229, 244.89752, 244.74869, 244.57428, 244.37299, 244.15114, 243.91817, 243.68317, 243.45407, 243.23892, 243.04678, 242.88657, 242.76321, 242.67384, 242.60654, 242.54338, 242.46664, 242.36465, 242.23463, 242.08151, 241.91415, 241.74152, 241.57103, 241.40913, 241.26248, 241.13812, 241.04169, 240.97488, 240.93446, 240.91347, 240.90419, 240.90033, 240.89764, 240.89319, 240.88458, 240.86954, 240.84596, 240.81187, 240.76492, 240.70248, 240.62254, 240.52585, 240.41753, 240.30713, 240.20618, 240.12434, 240.06625, 240.03062, 240.01196, 240.00343, 239.99907, 239.99397, 239.98354, 239.96288, 239.92747, 239.87463, 239.80496, 239.72218, 239.63187, 239.53944, 239.4493, 239.36465, 239.28859, 239.22404, 239.17308, 239.13513, 239.1059, 239.07784, 239.04247, 238.99342, 238.9287, 238.85092, 238.76582, 238.67937, 238.59517, 238.51289, 238.42818, 238.33414, 238.22444, 238.09679, 237.95541, 237.8111, 237.67786, 237.56741, 237.48404, 237.42189, 237.36688, 237.30197, 237.21352, 237.09567, 236.95099, 236.78748, 236.6143, 236.43845, 236.26334, 236.08937, 235.91527, 235.73933, 235.56042, 235.3782, 235.19316, 235.00607, 234.81775, 234.62869, 234.43929, 234.24973, 234.06007, 233.8701, 233.67889, 233.48473, 233.28493, 233.0766, 232.85741, 232.6263, 232.38348, 232.12984, 231.86658, 231.5957, 231.32114, 231.04918, 230.78767, 230.54359, 230.3204, 230.11671, 229.92719, 229.74512, 229.56474, 229.38274, 229.19804, 229.01109, 228.8228, 228.63399, 228.44514, 228.25642, 228.06786, 227.87936])

xdata = (1/(3.24 * 10 ** (-17))) * np.array([ 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3.0, 3.05, 3.1, 3.15, 3.2, 3.25, 3.3, 3.35, 3.4, 3.45, 3.5, 3.55, 3.6, 3.65, 3.7, 3.75, 3.8, 3.85, 3.9, 3.95, 4.0, 4.05, 4.1, 4.15, 4.2, 4.25, 4.3, 4.35, 4.4, 4.45, 4.5, 4.55, 4.6, 4.65, 4.7, 4.75, 4.8, 4.85, 4.9, 4.95, 5.0, 5.05, 5.1, 5.15, 5.2, 5.25, 5.3, 5.35, 5.4, 5.45, 5.5, 5.55, 5.6, 5.65, 5.7, 5.75, 5.8, 5.85, 5.9, 5.95, 6.0, 6.05, 6.1, 6.15, 6.2, 6.25, 6.3, 6.35, 6.4, 6.45, 6.5, 6.55, 6.6, 6.65, 6.7, 6.75, 6.8, 6.85, 6.9, 6.95, 7.0, 7.05, 7.1, 7.15, 7.2, 7.25, 7.3, 7.35, 7.4, 7.45, 7.5, 7.55, 7.6, 7.65, 7.7, 7.75, 7.8, 7.85, 7.9, 7.95, 8.0, 8.05, 8.1, 8.15, 8.2, 8.25, 8.3, 8.35, 8.4, 8.45, 8.5, 8.55, 8.6, 8.65, 8.7, 8.75, 8.8, 8.85, 8.9, 8.95, 9.0, 9.05, 9.1, 9.15, 9.2, 9.25, 9.3, 9.35, 9.4, 9.45, 9.5, 9.55, 9.6, 9.65, 9.7, 9.75, 9.8, 9.85, 9.9, 9.95, 10.0, 10.05, 10.1, 10.15, 10.2, 10.25, 10.3, 10.35, 10.4, 10.45, 10.5, 10.55, 10.6, 10.65, 10.7, 10.75, 10.8, 10.85, 10.9, 10.95, 11.0, 11.05, 11.1, 11.15, 11.2, 11.25, 11.3, 11.35, 11.4, 11.45, 11.5, 11.55, 11.6, 11.65, 11.7, 11.75, 11.8, 11.85, 11.9, 11.95, 12.0, 12.05, 12.1, 12.15, 12.2, 12.25, 12.3, 12.35, 12.4, 12.45, 12.5, 12.55, 12.6, 12.65, 
12.7, 12.75, 12.8, 12.85, 12.9, 12.95, 13.0, 13.05, 13.1, 13.15, 13.2, 13.25, 13.3, 13.35, 13.4, 13.45, 13.5, 13.55, 13.6, 13.65, 13.7, 13.75, 13.8, 13.85, 13.9, 13.95, 14.0, 14.05, 14.1, 14.15, 14.2, 14.25, 14.3, 14.35, 14.4, 14.45, 14.5, 14.55, 14.6, 14.65, 14.7, 14.75, 14.8, 14.85, 14.9, 14.95, 15.0, 15.05, 15.1, 15.15, 15.2, 15.25, 15.3, 15.35, 15.4, 15.45, 15.5, 15.55, 15.6, 15.65, 15.7, 
15.75, 15.8, 15.85, 15.9, 15.95, 16.0, 16.05, 16.1, 16.15, 16.2, 16.25, 16.3, 16.35, 16.4, 16.45, 16.5, 16.55, 16.6, 16.65, 16.7, 16.75, 16.8, 16.85, 16.9, 16.95, 17.0, 17.05, 17.1, 17.15, 17.2, 17.25, 17.3, 17.35, 17.4, 17.45, 17.5, 17.55, 17.6, 17.65, 17.7, 17.75, 17.8, 17.85, 17.9, 17.95, 18.0, 18.05, 18.1, 18.15, 18.2, 18.25, 18.3, 18.35, 18.4, 18.45, 18.5, 18.55, 18.6, 18.65, 18.7, 18.75, 18.8, 18.85, 18.9, 18.95, 19.0, 19.05, 19.1, 19.15, 19.2, 19.25, 19.3, 19.35, 19.4, 19.45, 19.5, 19.55, 19.6, 19.65, 19.7, 19.75, 19.8, 19.85, 19.9, 19.95, 20.0, 20.05, 20.1, 20.15, 20.2, 20.25, 20.3, 20.35, 20.4, 20.45, 20.5, 20.55, 20.6, 20.65, 20.7, 20.75, 20.8, 20.85, 20.9, 20.95, 21.0, 21.05, 21.1, 21.15, 21.2, 21.25, 21.3, 21.35, 21.4, 21.45, 21.5, 21.55, 21.6, 21.65, 21.7, 21.75, 21.8, 21.85, 21.9, 21.95, 22.0, 22.05, 22.1, 22.15, 22.2, 22.25, 22.3, 22.35, 22.4, 22.45, 22.5, 22.55, 22.6, 22.65, 22.7, 22.75, 22.8, 22.85, 22.9, 22.95, 23.0, 23.05, 23.1, 23.15, 23.2, 23.25, 23.3, 23.35, 23.4, 23.45, 23.5, 23.55, 23.6, 23.65, 23.7, 23.75, 23.8, 23.85, 23.9, 23.95, 24.0, 24.05, 24.1, 24.15, 24.2, 24.25, 24.3, 24.35, 24.4, 24.45, 24.5, 24.55, 24.6, 24.65, 24.7, 24.75, 24.8, 24.85, 24.9, 24.95, 25.0, 25.05, 25.1, 25.15, 25.2, 25.25, 25.3, 25.35, 25.4, 25.45, 25.5, 25.55, 25.6, 25.65, 25.7, 25.75, 25.8, 25.85, 
25.9, 25.95, 26.0, 26.05, 26.1, 26.15, 26.2, 26.25, 26.3, 26.35, 26.4, 26.45, 26.5, 26.55, 26.6, 26.65, 26.7, 26.75, 26.8, 26.85, 26.9, 26.95, 27.0, 27.05, 27.1, 27.15, 27.2, 27.25, 27.3, 27.35, 27.4, 27.45, 27.5, 27.55, 27.6, 27.65, 27.7, 27.75, 27.8, 27.85, 27.9, 27.95, 28.0, 28.05, 28.1, 28.15, 28.2, 28.25, 28.3, 28.35, 28.4, 28.45, 28.5, 28.55, 28.6, 28.65, 28.7, 28.75, 28.8, 28.85, 28.9, 
28.95, 29.0, 29.05, 29.1, 29.15, 29.2, 29.25, 29.3, 29.35, 29.4, 29.45, 29.5, 29.55, 29.6, 29.65, 29.7, 29.75, 29.8, 29.85, 29.9, 29.95, 30.0, 30.05, 30.1, 30.15, 30.2, 30.25, 30.3, 30.35, 30.4, 30.45, 30.5, 30.55, 30.6, 30.65, 30.7, 30.75, 30.8, 30.85, 30.9, 30.95, 31.0, 31.05, 31.1, 31.15, 31.2, 31.25])

#print(scp.curve_fit(f,xdata,vf))
#result = (array([9.57044233e-17]), array([[5.90623158e-35]])) : a = 2.95


ydata =   f(xdata,9.57044233e-17) +220

plt.plot(xdata,ydata, label = 'model')
plt.plot(xdata,vf, label = 'data')
plt.xlabel('radius, km')
plt.ylabel('orbital speed, km/s')
plt.legend()
plt.show()