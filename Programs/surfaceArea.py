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
    print("--- Given a Spherical Tank ---")
    print("=" * 50)
    radiusSphere = int(input("Enter the radius (meters): ").strip())

    surfaceAreaSphere = 4 * np.pi * radiusSphere**2

    print(f"\n")
    print("Result:")
    print("──────────────────────────────────────────────────") 
    print(f"| Radius                | {radiusSphere} m\n")

    print(f"Total surface area = {round(surfaceAreaSphere, 2)} m²")

def ConeSurfaceArea():
    print("--- Given a Conical Tank ---")
    print("=" * 50)   
    radCone = int(input("Enter the radius (meters): ").strip())
    heightCone = int(input("Enter the height (meters): ").strip())

    baseAreaCone = np.pi * radCone**2
    latAreaCone = np.pi * radCone * np.sqrt(radCone**2 + heightCone**2)
    surfaceAreaCone = baseAreaCone + latAreaCone

    print(f"\n")
    print("Result:")
    print("──────────────────────────────────────────────────") 
    print(f"| Radius                | {radCone} m")
    print(f"| Height                | {round(heightCone, 2)} m")
    print(f"| Base surface area     | {round(baseAreaCone, 2)} m²")
    print(f"| Lateral surface area  | {round(latAreaCone, 2)} m²\n")

    print(f"Total surface area = {round(surfaceAreaCone, 2)} m²")


def CubeSurfaceArea():
    print("--- Given a Cubical Tank ---")
    print("=" * 50)
    edgeLengthCube = int(input(f"Enter the edge length (meters): ").strip())
    surfaceAreaCube = 6 * edgeLengthCube**2
    
    print(f"\n")
    print("Result:")
    print("──────────────────────────────────────────────────") 
    print(f"| Edge length                | {edgeLengthCube} m\n")

    print(f"Total surface area = {round(surfaceAreaCube, 2)} m²")


def CylindricalSurfaceArea():
    print(f"--- Given a Cylidrical Tank ---")
    print("=" * 50)
    baseRadCyl = int(input("Enter the base radius: ").strip())
    heightCyl = int(input("Enter the base height (meters): ").strip())

    topAreaCyl = np.pi * baseRadCyl**2
    botAreaCyl = topAreaCyl
    latAreaCyl = 2 * np.pi * baseRadCyl * heightCyl
    surfaceAreaCyl = topAreaCyl + botAreaCyl + latAreaCyl
  
    print(f"\n")
    print("Result:")
    print("──────────────────────────────────────────────────") 
    print(f"| Base radius           | {baseRadCyl} m")
    print(f"| Top surface area      | {round(topAreaCyl, 2)} m²")
    print(f"| Bottom surface area   | {round(botAreaCyl, 2)} m²")
    print(f"| Lateral surface area  | {round(latAreaCyl, 2)} m²\n")

    print(f"Total surface area = {round(surfaceAreaCyl, 2)} m²")


def SphericalCapSurfaceArea():
    print("--- Given a Spherocylinder Tank ---")
    print("=" * 50)
    baseRadSphereCap = int(input("Enter the base radius: ").strip())
    heightSphereCap = int(input("Enter the height: ").strip())

    topAreaSphereCap = 2 * np.pi * baseRadSphereCap
    botAreaSphereCap = topAreaSphereCap
    latAreaSphereCap = 2 * np.pi * baseRadSphereCap * heightSphereCap
    surfaceAreaSphereCap = topAreaSphereCap + botAreaSphereCap + latAreaSphereCap

    print(f"\n")
    print("Result:")
    print("──────────────────────────────────────────────────") 
    print(f"| Base radius           | {baseRadSphereCap} m")
    print(f"| Height                | {heightSphereCap} m")
    print(f"| Top surface area      | {round(topAreaSphereCap, 2)} m²")
    print(f"| Bottom surface area   | {round(botAreaSphereCap, 2)} m²")
    print(f"| Lateral surface area  | {round(latAreaSphereCap, 2)} m²\n")

    print(f"Total surface area = {round(surfaceAreaSphereCap,2)} m²")
   

def capSurfaceArea():
    print("--- Given a Hemispherical Tank")
    print("=" * 50)
    baseRadCap = int(input("Enter the base radius: ").strip())
    ballRadCap = int(input("Enter the ball radius: ").strip())
    heightCap = int(input("Enter the height: ").strip())

    heightCap1 = ballRadCap - np.sqrt(ballRadCap**2 - baseRadCap**2)
    baseAreaCap1 = np.pi * baseRadCap**2
    capArea1 = 2 * np.pi * heightCap1 * ballRadCap
    surfaceAreaCap1 = baseAreaCap1 + capArea1

    heightCap2 = ballRadCap + np.sqrt(ballRadCap**2 - baseRadCap**2) 
    baseAreaCap2 = np.pi * baseRadCap**2
    capArea2 = 2 * np.pi * heightCap2 * ballRadCap
    surfaceAreaCap2 = baseAreaCap2 + capArea2

    print(f"\n")
    print("Result 1:")
    print("──────────────────────────────────────────────────") 
    print(f"Base radius             | {baseRadCap} m")
    print(f"Ball radius             | {ballRadCap} m")
    print(f"Height                  | {round(heightCap1, 2)} m")
    print(f"Base surface area       | {round(baseAreaCap1, 2)} m²")
    print(f"Cap surface area        | {round(capArea1, 2)} m²\n")
    print(f"Total surface area = {round(surfaceAreaCap1, 2)} m²")

    print(f"\nor\n")

    print(f"Result 2:")
    print("──────────────────────────────────────────────────")        
    print(f"Base radius             | {baseRadCap} m")
    print(f"Ball radius             | {ballRadCap} m")
    print(f"Height                  | {round(heightCap2, 2)} m")
    print(f"Base surface area       | {round(baseAreaCap2, 2)} m²")
    print(f"Cap surface area        | {round(capArea2, 2)} m²\n")
    print(f"Total surface area = {round(surfaceAreaCap2, 2)} m²")


def coneFrustumSurfaceArea():
    print("--- Given a Truncated Conical Tank ---")
    print("=" * 50)
    topRadFrustum = int(input("Enter the upper radius: ").strip())
    botRadFrustum = int(input("Enter the base radius: ").strip())
    heightFrustum = int(input("Enter the height: ").strip())

    topAreaFrustum = np.pi * topRadFrustum**2
    botAreaFrustum = np.pi * botRadFrustum**2
    latAreaFrustum = np.pi * (botRadFrustum + topRadFrustum) * np.sqrt((botRadFrustum - topRadFrustum)**2 + heightFrustum)
    surfaceAreaFrustum = topAreaFrustum + botAreaFrustum + latAreaFrustum

    print(f"\n")

    print(f"Result :")
    print("──────────────────────────────────────────────────")        
    print(f"Top radius              | {topRadFrustum} m")
    print(f"Bottom radius           | {botRadFrustum} m")
    print(f"Height                  | {round(heightFrustum, 2)} m")
    print(f"Top surface area        | {round(topAreaFrustum, 2)} m²")
    print(f"Bottom Surface Area     | {round(botAreaFrustum, 2)} m²")
    print(f"Lateral Surface Area    | {round(latAreaFrustum, 2)} m²\n")
    print(f"Total surface area = {round(surfaceAreaFrustum, 2)} m²")


def ellipsoidSurfaceArea():
    print("--- Given an Elliptical Tank ---")
    print("=" * 50)
    axis1E = int(input("Enter axis 1: ").strip())
    axis2E = int(input("Enter axis 2: ").strip())
    axis3E = int(input("Enter axis 3: ").strip())
    surfaceAreaEllipsoid = 4 * np.pi * (((axis1E * axis2E)**1.6 + (axis1E * axis3E)**1.6 + (axis2E * axis3E)**1.6) / 3)**(1/1.6)
    

    print(f"\n")

    print(f"Result :")
    print("──────────────────────────────────────────────────")        
    print(f"Axis 1              | {round(axis1E, 2)} m")
    print(f"Axis 2              | {round(axis2E, 2)} m")
    print(f"Axis 3              | {round(axis3E, 2)} m\n")
    print(f"Total surface area = {round(surfaceAreaEllipsoid, 2)} m²")



def main():
    print(f"What shape do you want to find the surface area of? (given m = meters)\n")
    print("─────────────────────────────────────────────────────────────")                              
    print("Sphere (G1) | Cone (G2) | Cube (G3) | Cylinder (G4) | Spherocylinder (G4) | Hemisphere (G5) | Conical Frustum (G6) | Ellipsoid (G7)")
    print("─────────────────────────────────────────────────────────────")
    measureArea = input(f"Enter a shape to calculate: ").strip().lower()
    print(f"\n")
    if measureArea == "g1":
        SphereSurfaceArea()
    elif measureArea == "g2":
        ConeSurfaceArea()
    elif measureArea == "g2":
        CubeSurfaceArea()
    elif measureArea == "g3":
        CylindricalSurfaceArea()
    elif measureArea == "g4":
        SphericalCapSurfaceArea()
    elif measureArea == "g5":
        capSurfaceArea()
    elif measureArea == "g6":
        coneFrustumSurfaceArea()
    elif measureArea == "g7":
        ellipsoidSurfaceArea()
if __name__ == "__main__":
    main()