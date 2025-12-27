import matplotlib.pyplot as pt


def focus_graph():
    try:
        with open("focus.txt", "r") as file:
            content = file.read()

        # Split and filter out empty strings
        content = [float(i.strip()) for i in content.split(",") if i.strip() != ""]

        x1 = list(range(len(content)))
        y1 = content

        print(content)

        pt.plot(x1, y1, color="red", marker="o")
        pt.title("YOUR FOCUSED TIME", fontsize=16)
        pt.xlabel("Times", fontsize=14)
        pt.ylabel("Focus Time", fontsize=14)
        pt.grid()
        pt.show()

    except FileNotFoundError:
        print("focus.txt not found!")
    except ValueError as e:
        print(f"Data formatting issue: {e}")
