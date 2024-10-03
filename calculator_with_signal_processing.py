import numpy as np
import matplotlib.pyplot as plt

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to generate and display a sine wave based on user input
def generate_sine_wave(frequency, amplitude, duration=1, sample_rate=500):
    t = np.linspace(0, duration, sample_rate)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, y

# Function to let user create multiple sine waves and plot their sum
def add_sine_waves():
    total_waves = int(input("How many sine waves would you like to add? "))
    t = np.linspace(0, 1, 500)  # Time array for plotting
    combined_wave = np.zeros(500)  # Initialize the combined wave
    
    # Loop for each wave the user wants to create
    for i in range(total_waves):
        print(f"Wave {i + 1}:")
        frequency = float(input("Enter the frequency of the sine wave (in Hz): "))
        amplitude = float(input("Enter the amplitude of the sine wave: "))
        t, wave = generate_sine_wave(frequency, amplitude)
        combined_wave += wave
    
    # Ask the user if they want to save the graph before showing
    save_choice = input("Do you want to save the graph? (yes/no): ").lower()
    if save_choice == 'yes':
        filename = input("Enter the filename (with .png extension): ")
        plt.figure(figsize=(10, 6))
        plt.plot(t, combined_wave, label="Combined Wave")
        plt.title('Sum of Multiple Sine Waves')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid(True)
        plt.savefig(filename)
        print(f"Graph saved as {filename}.")
    
    # Plot the combined wave
    plt.figure(figsize=(10, 6))
    plt.plot(t, combined_wave, label="Combined Wave")
    plt.title('Sum of Multiple Sine Waves')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

# Function to perform Fourier Transform and plot
def fourier_transform():
    # Generate a signal (sine wave)
    t = np.linspace(0, 1, 500)
    signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

    # Perform Fourier Transform
    freq = np.fft.fftfreq(t.size, t[1] - t[0])
    fft_signal = np.fft.fft(signal)

    # Plot the original signal
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(t, signal)
    plt.title("Original Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    # Plot the Fourier Transform (Magnitude)
    plt.subplot(1, 2, 2)
    plt.plot(freq[:len(freq)//2], np.abs(fft_signal[:len(freq)//2]))
    plt.title("Fourier Transform")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show(block=False)

# Main program
def calculator():
    print("Welcome to the Calculator and Signal Processing App")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Generate and Add Sine Waves")
    print("6. Perform Fourier Transform")
    print("Enter 'q' to quit.")
    
    while True:
        choice = input("Enter choice(1/2/3/4/5/6 or 'q' to quit): ")
        
        if choice == 'q':
            print("Exiting the application.")
            break
        
        elif choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
                
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
                
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
                
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print("Generating and Adding Multiple Sine Waves...")
            add_sine_waves()

        elif choice == '6':
            print("Performing Fourier Transform on a signal...")
            fourier_transform()

        else:
            print("Invalid input. Please choose a valid option.")
        
        # Check if the user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Thank you for using the calculator and signal processing app!")

# Run the calculator
calculator()
