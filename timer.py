import tkinter as TK
import datetime

class countdown:
    def __init__(self, master, time): 
        self.master = master
        self.master.title("Final Countdown")
        self.frame = TK.Frame(self.master)
        self.targetTime = datetime.datetime.strptime(time, "%d/%m/%y %H:%M:%S")
        self.timeRemainingLabel = TK.Label(self.frame, bg="black", fg="red", font=("Consolas Bold Italic", 28), height=2, width=25)
        self.startButton = TK.Button(self.frame, text="Countdown", command=lambda:self.master.after(1000, self.update))
        self.endTimeLabel = TK.Label(self.frame, text="Target time:")
        self.main_titleLabel = TK.Label(self.frame, text="Final Countdown !!!", font=("Calibri Bold", 16))
        self.endTimeEntry = TK.Entry(self.frame)
        self.endTimeEntry.insert(0, time)
        self.frame.grid()
        self.main_titleLabel.grid(row=1,column=1, columnspan=3)
        self.timeRemainingLabel.grid(row=2,column=1, columnspan=3)
        self.startButton.grid(row=3, column=1, rowspan=2)
        self.endTimeLabel.grid(row=3, column=2)
        self.endTimeEntry.grid(row=4, column=2)

    def update(self):
        remaining = self.targetTime-datetime.datetime.now()
        daysRemaining = remaining.days
        hoursRemaining = int(int(remaining.seconds) / 3600)
        minutesRemaining = int(int(remaining.seconds % 3600) / 60)
        secondsRemaining = int(int(remaining.seconds % 60))
        self.timeRemainingLabel.config(text="{days} jours {hours}h {minutes}m {seconds}s" \
            .format(
                targetTime=datetime.datetime.strptime(self.endTimeEntry.get(), "%d/%m/%y %H:%M:%S"), 
                days=daysRemaining, 
                hours=hoursRemaining, 
                minutes=minutesRemaining, 
                seconds=secondsRemaining
                )
            )
        self.master.after(1000, self.update)

root = TK.Tk()
c = countdown(root, "01/07/23 00:00:00")
root.mainloop()