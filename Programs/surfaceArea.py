# Assembly (HLA) >>>> Python Code Translation

"""asm
program SphereSurfaceArea;
#include("stdlib.hhf");

static
    radius : real32;
    area   : real32;

begin SphereSurfaceArea;

    stdout.put("Enter the radius: ");
    stdin.get(radius);

    fld(radius);     // Pushes radius onto the FPU stack [ST(0)]
    fld(radius);     // Pushes radius onto the FPU stack [ST(1), ST(0)]
    fmul;            // Multiplies ST(0) by ST(1), stores in ST(0)
    fldpi;           // Pushes the value of pi onto the FPU stack [ST(2), ST(1), ST(0)]
    fmul;            // Multiplies ST(0) (radius^2) by ST(1) (pi)
    fmul;            // Multiplies ST(0) (pi*r^2) by 4 (surface area = 4 * pi * r^2)
    
    fstp(area);      // Pops the result from the FPU stack and stores in 'area'

    stdout.put("Surface Area = ", area);

end SphereSurfaceArea;
"""

import numpy as np

def SphereSurfaceArea():
    radiusSphere = int(input("Enter the radius: ").strip())
    surfaceAreaSphere = 4 * np.pi * radiusSphere**2
    """DEBUG
    print(f"surfaceArea: {surfaceAreaS}")
    """
    print("=" * 80)
    print(f"A sphere with a radius {radiusSphere} m, has a surface area of {round(surfaceAreaSphere, 2)} m².\n")
    print(f"Given m = meters")
    print("=" * 80)

def ConeSurfaceArea():
    radiusCone = int(input("Enter the radius: ").strip())
    heightCone = int(input("Enter the height: ").strip())
    baseSurfaceAreaCone = np.pi * radiusCone**2
    latSurfaceAreaCone = np.pi * radiusCone * np.sqrt(radiusCone**2 + heightCone**2)
    """ DEBUG
    print(f"Base surface area: {baseSurfaceAreaC}")
    print(f"Lateral surface area: {latSurfaceAreaC}")
    """
    surfaceAreaCone = baseSurfaceAreaCone + latSurfaceAreaCone
    print("=" * 80)
    print(f"A cone with a radius {radiusCone} m and a height {heightCone} m, has a surface area of {round(surfaceAreaCone, 2)} m².\n")
    print("Given m = meters")
    print("=" * 80)
def CubeSurfaceArea():
    edgeLengthCube = int(input(f"Enter the edge length: ").strip())
    surfaceAreaCube = 6 * edgeLengthCube**2
    
    print("=" * 80)
    print(f"A cube with an edge length {edgeLengthCube} m, has a surface area of {surfaceAreaCube} m².\n")
    print("Given m = meters")
    print("=" * 80)

def main():
    print("What shape do you want to find the surface area of?") # choose the shape to calculate the surface area of
    print(f"| Sphere | Cone | Cube | \n")
    measureArea = input(f"Enter a shape to calculate: ").strip().lower()
    print(f"\n")
    if measureArea == "sphere":
        SphereSurfaceArea()
    elif measureArea == "cone":
        ConeSurfaceArea()
    elif measureArea == "cube":
        CubeSurfaceArea()

if __name__ == "__main__":
    main()