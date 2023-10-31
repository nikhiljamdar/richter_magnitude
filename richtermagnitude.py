user=float(input("Enter value:"))

if user>1.0 and user<=2.0:
    print("Microearthquakes not felt or rarely felt")
elif user>=2.0 and user<=4.0:
    print("Very rarely causes damage")
elif user>=4.0 and user<=5.0:
    print("Damage done to weak buildings")
elif user>=5.0 and user<=6.0:
    print("Cause damage to the poorly constructed building")
elif user>=6.0 and user<=7.0:
    print("Causes damage to well-built structures")
elif user>=7.0 and user<=8.0:
    print("Causes damage to most buildings")
elif user>=8.0 and user<=9.0:
    print("Causes major destruction")
elif user>=9.0:
    print("Causes unbelievable damage")
else:
    print("Richter magnitude value is not defined")
