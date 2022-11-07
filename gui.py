# -*- coding: utf-8 -*-

# Code was written by Hendrik Lanz with the help of PyQt5 UI code generator 5.15.4
#Contact:
#       Email: name42@riseup.net
#       GitHub: pythondealer
# 


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog

from steganographer import magicBytes
from steganographer import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 641)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Headline = QtWidgets.QLabel(self.centralwidget)
        self.Headline.setGeometry(QtCore.QRect(330, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Headline.setFont(font)
        self.Headline.setStyleSheet("color: rgb(189, 24, 123);")
        self.Headline.setObjectName("Headline")

        self.Button_restore = QtWidgets.QPushButton(self.centralwidget)
        self.Button_restore.setGeometry(QtCore.QRect(590, 430, 131, 61))
        self.Button_restore.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Button_restore.setObjectName("Button_restore")
        self.Button_restore.clicked.connect(self.restore)

        self.Button_hide = QtWidgets.QPushButton(self.centralwidget)
        self.Button_hide.setGeometry(QtCore.QRect(170, 430, 131, 61))
        self.Button_hide.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Button_hide.setObjectName("Button_hide")
        self.Button_hide.clicked.connect(self.hide)

        self.le_img_in_hide = QtWidgets.QLineEdit(self.centralwidget)
        self.le_img_in_hide.setGeometry(QtCore.QRect(180, 150, 113, 24))
        self.le_img_in_hide.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.le_img_in_hide.setObjectName("le_img_in_hide")

        self.le_file_hide = QtWidgets.QLineEdit(self.centralwidget)
        self.le_file_hide.setGeometry(QtCore.QRect(180, 200, 113, 24))
        self.le_file_hide.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.le_file_hide.setObjectName("le_file_hide")

        self.le_output_hide = QtWidgets.QLineEdit(self.centralwidget)
        self.le_output_hide.setGeometry(QtCore.QRect(180, 250, 113, 24))
        self.le_output_hide.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.le_output_hide.setObjectName("le_output_hide")

        self.le_pw_hide = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pw_hide.setGeometry(QtCore.QRect(180, 300, 113, 24))
        self.le_pw_hide.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.le_pw_hide.setObjectName("le_pw_hide")
        self.le_pw_hide.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 150, 111, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 71, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 250, 81, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 300, 58, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 150, 111, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 200, 111, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 250, 111, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")

        self.le_img_in_ex = QtWidgets.QLineEdit(self.centralwidget)
        self.le_img_in_ex.setGeometry(QtCore.QRect(610, 150, 113, 24))
        self.le_img_in_ex.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.le_img_in_ex.setObjectName("le_img_in_ex")

        self.le_output_path_ex = QtWidgets.QLineEdit(self.centralwidget)
        self.le_output_path_ex.setGeometry(QtCore.QRect(610, 200, 113, 24))
        self.le_output_path_ex.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.le_output_path_ex.setObjectName("le_output_path_ex")

        self.le_pw_ex = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pw_ex.setGeometry(QtCore.QRect(610, 250, 113, 24))
        self.le_pw_ex.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.le_pw_ex.setObjectName("le_pw_ex")
        self.le_pw_ex.setEchoMode(QtWidgets.QLineEdit.Password)

        self.r_Button_lsb = QtWidgets.QRadioButton(self.centralwidget)
        self.r_Button_lsb.setGeometry(QtCore.QRect(180, 350, 111, 22))
        self.r_Button_lsb.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.r_Button_lsb.setObjectName("r_Button_lsb")
        self.r_Button_lsb.setChecked(True)

        self.r_Button_end = QtWidgets.QRadioButton(self.centralwidget)
        self.r_Button_end.setGeometry(QtCore.QRect(180, 370, 111, 22))
        self.r_Button_end.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.r_Button_end.setObjectName("r_Button_end")

        self.Browse_button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_button_1.setGeometry(QtCore.QRect(320, 150, 80, 24))
        self.Browse_button_1.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Browse_button_1.setObjectName("Browse_button_1")
        self.Browse_button_1.clicked.connect(lambda:self.open_img("Browse_button_1"))

        self.Browse_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_button_2.setGeometry(QtCore.QRect(320, 200, 80, 24))
        self.Browse_button_2.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Browse_button_2.setObjectName("Browse_button_2")
        self.Browse_button_2.clicked.connect(self.open_file)

        self.Browse_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_button_3.setGeometry(QtCore.QRect(320, 250, 80, 24))
        self.Browse_button_3.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Browse_button_3.setObjectName("Browse_button_3")
        self.Browse_button_3.clicked.connect(self.save_img)

        self.Browse_button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_button_4.setGeometry(QtCore.QRect(740, 150, 80, 24))
        self.Browse_button_4.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Browse_button_4.setObjectName("Browse_button_4")
        self.Browse_button_4.clicked.connect(lambda:self.open_img("Browse_button_4"))

        self.Browse_Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_Button_5.setGeometry(QtCore.QRect(740, 200, 80, 24))
        self.Browse_Button_5.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.Browse_Button_5.setObjectName("Browse_Button_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Browse_Button_5.clicked.connect(self.save_file)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganographer"))
        self.Headline.setText(_translate("MainWindow", "Steganographer"))
        self.Button_restore.setText(_translate("MainWindow", "Restore a file"))
        self.Button_hide.setText(_translate("MainWindow", "Hidea file"))
        self.label.setText(_translate("MainWindow", "Image input path"))
        self.label_2.setText(_translate("MainWindow", "File to hide"))
        self.label_3.setText(_translate("MainWindow", "Outputpath"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Input image"))
        self.label_6.setText(_translate("MainWindow", "Outputpath"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.r_Button_lsb.setText(_translate("MainWindow", "lsb-mode"))
        self.r_Button_end.setText(_translate("MainWindow", "End-mode"))
        self.Browse_button_1.setText(_translate("MainWindow", "Browse"))
        self.Browse_button_2.setText(_translate("MainWindow", "Browse"))
        self.Browse_button_3.setText(_translate("MainWindow", "Browse"))
        self.Browse_button_4.setText(_translate("MainWindow", "Browse"))
        self.Browse_Button_5.setText(_translate("MainWindow", "Browse"))

    def open_img(self, n):
        file_ = (QtWidgets.QFileDialog.getOpenFileName(filter= "*.png"))
        file_ = file_[0]

        if n == "Browse_button_1":## NUR PNG ERLAUBEN
            self.le_img_in_hide.setText('{}'.format(file_))

        if n == "Browse_button_4":
            self.le_img_in_ex.setText('{}'.format(file_))


    def save_img(self):

        save_filename = (QtWidgets.QFileDialog.getSaveFileName(None, "Select destination folder and file name", "outpu1", "PNG files (*.png)")[0])


        if not save_filename or save_filename != '.png':
            save_filename = save_filename + '.png'


        self.le_output_hide.setText('{}'.format(save_filename))


    def open_file(self):
        file_ = (QtWidgets.QFileDialog.getOpenFileName())
        file_ = file_[0]

        self.le_file_hide.setText('{}'.format(file_))

    def save_file(self):
        save_filename = (QtWidgets.QFileDialog.getSaveFileName()[0])

        self.le_output_path_ex.setText('{}'.format(save_filename))

    

    def hide(self):
        
        try:        
            if self.r_Button_lsb.isChecked():
                hidingMode = "lsb"                

            if self.r_Button_end.isChecked():
                hidingMode == "endian"


            inputImagePath = self.le_img_in_hide.text()
            fileToHidePath = self.le_file_hide.text()
            outputImagePath = self.le_output_hide.text()
            password = self.le_pw_hide.text()

            
            size_err = hideDataToImage(inputImagePath, fileToHidePath, outputImagePath, password, hidingMode)
            if size_err == True:
                size_err_msg = QMessageBox()
                size_err_msg.setWindowTitle(size_err)
                size_err_msg.setText("The file you want to hide is to big. Please selected a bigger picture or choose a smaller file")
                size_err_msg_exec = size_err_msg.exec_()

            if size_err != True:
                

                #Ask if the orginal file should be safly removed
                dialog_text = ("Should the original file be deleted in a safe way (recommended)?.

                del_request = QMessageBox()
                del_request.setIcon(QMessageBox.Question)     
                del_request.setWindowTitle("Delete original file?")
                del_request.setText(dialog_text)
                del_request.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                call_del = del_request.exec_()

                if call_del == QMessageBox.Yes:
                    remove_from_drive(fileToHidePath)

                msg_sucsess = QMessageBox()
                msg_sucsess.setWindowTitle("success")
                msg_sucsess.setText("File successfully hidden")
                x = msg_sucsess.exec_()

                self.le_img_in_hide.setText("")
                self.le_file_hide.setText("")
                self.le_output_hide.setText("")
                self.le_pw_hide.setText("")
        
        except Exception as e:
            print("The error raised is: ", e)

            e = str(e)
            fail_msg_text = ("Sorry, something went wrong. The error raised is" + e)

            msg_fail = QMessageBox()
            msg_fail.setWindowTitle("Failed")
            msg_fail.setText(fail_msg_text)
            y = msg_fail.exec_()

            self.le_img_in_hide.setText("")
            self.le_file_hide.setText("")
            self.le_output_hide.setText("")
            self.le_pw_hide.setText("")


    def restore(self):

        try:
            pw_err = False
            inputImagePath = self.le_img_in_ex.text()
            outputFilePath = self.le_output_path_ex.text()
            password = self.le_pw_ex.text()
        
            pw_err = extractDataFromImage(inputImagePath, outputFilePath, password)

            if pw_err != True:
                msg_sucsess = QMessageBox()
                msg_sucsess.setWindowTitle("sucsess")
                msg_sucsess.setText("File sucsessfully extracted")
                x = msg_sucsess.exec_()

                self.le_img_in_ex.setText("")
                self.le_output_path_ex.setText("")
                self.le_pw_ex.setText("")

            if pw_err == True:
                pw_fail = QMessageBox()
                pw_fail.setWindowTitle("Wrong password")
                pw_fail.setText("Wrong password")
                pw_fail_exec = pw_fail.exec_()

        except Exception as e:

            fail_msg =("Sorry, something went wrong" + e)

            msg_fail = QMessageBox()
            msg_fail.setWindowTitle("Failed")
            msg_fail.setText(fail_msg)
            x = msg_fail.exec_()        


            self.le_img_in_ex.setText("")
            self.le_output_path_ex.setText("")
            self.le_pw_ex.setText("")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
