from tkinter import * #Tk, StringVar, IntVar, Button, Radiobutton, Label, Entry, OptionMenu, Checkbutton, filedialog, _setit
from tkinter import _setit, filedialog



# Create interface window object
root = Tk()
root.title('HPX dynamic data analysis')
root.geometry('1300x400')



calcLV_method = StringVar(None, 'Pneumotach')
calcLV_pneumo = Radiobutton(root, text = 'Pneumotach', value = 'Pneumotach', variable = calcLV_method)
calcLV_pneumo.place(x = 320, y = 185)
calcLV_signal = Radiobutton(root, text = 'Signal', value = 'Signal', variable = calcLV_method)
calcLV_signal.place(x = 320, y = 203)
calcLV_diaphragm = Radiobutton(root, text = 'Diaphragm', value = 'Diaphragm', variable = calcLV_method)
calcLV_diaphragm.place(x = 320, y = 221)

# ANALYSIS PARAMETER ENTRIES
# Matrix size entry
Label(root, text = 'Matrix size =').place(x = 10, y = 230)
MS_entry = Entry(root, width = 3)
MS_entry.insert(0, str(11))
MS_entry.place(x = 95, y = 230)

# Image size entry
Label(root, text = 'Image size  =').place(x = 10, y = 250)
IS_entry = Entry(root, width = 3)
IS_entry.insert(0, str(22))
IS_entry.place(x = 95, y = 250)

# Number of bins entry
Label(root, text = '# of bins   =').place(x = 10, y = 270)
nbins_entry = Entry(root, width = 3)
nbins_entry.insert(0, str(33))
nbins_entry.place(x = 95, y = 270)

# x,y,z kernel width
Label(root, text = 'Kernel dx  =').place(x = 10, y = 290)
xyz_kernel_entry = Entry(root, width = 3)
xyz_kernel_entry.insert(0, '1')
xyz_kernel_entry.place(x = 95, y = 290)

# t kernel width
Label(root, text = 'Kernel dt  =').place(x = 10, y = 310)
t_kernel_entry = Entry(root, width = 3)
t_kernel_entry.insert(0, '1')
t_kernel_entry.place(x = 95, y = 310)



# Execute tkinter
root.mainloop()