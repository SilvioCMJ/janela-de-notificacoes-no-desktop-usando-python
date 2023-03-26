from win10toast import ToastNotfier
#puxando lib
toaster = ToastNotfier()

#config notiicação
toaster.show_toast("Notificação", "Notificação funcionou ", threaded=True, icon_path=None, duration=3)
