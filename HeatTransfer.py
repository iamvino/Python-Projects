def heat_transfer(k, A, delta_T, d):
    Q = (k * A * delta_T) / d
    return Q

k = float(input("Enter the thermal conductivity (W/m·K): "))
A = float(input("Enter the surface area (m^2): "))
delta_T = float(input("Enter the temperature difference (K): "))
d = float(input("Enter the thickness of the medium (m): "))

result = heat_transfer(k, A, delta_T, d)
print("Heat transfer rate: {:.2f} Watts".format(result))
