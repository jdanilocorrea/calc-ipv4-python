
from template.ui_darthrede import Ui_MainWindow, QtCore, QtGui, QtWidgets
from template.calc_ipv4 import CalculateIP


class MainWindow(QtWidgets.QMainWindow,CalculateIP):
    def __init__(self,*args,**argvs):
        super(MainWindow,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)       
        
        self.ui.lineEdit_rede.setText('127.168.1.0')
        self.ui.lineEdit_mask.setText('255.255.255.240')
        self.ui.lineEdit_gateway.setText('192.168.0.1')

        self.ui.pushButton_calculate.clicked.connect(self.buttonCalculate)
        self.ui.pushButton_clear.clicked.connect(self.buttonClear)
    

    def buttonCalculate(self):
        
        ipv4_rede = self.ui.lineEdit_rede.text()
        mask_rede = self.ui.lineEdit_mask.text()
        # gateway_rede = self.ui.lineEdit_gateway.text()

        octets_rede_ipv4 = ipv4_rede.split('.')
        octets_mask = mask_rede.split('.')

        #Determina a classe de rede com o primeiro octeto
        octet1 = octets_rede_ipv4[0]   
        cl_rede = CalculateIP.classRede(octet1)
        self.ui.label_class_value.setText(cl_rede)

        #Converte IP em bits
        conv_bits_mask = CalculateIP.maskConvertBits(octets_mask)
        
        #Numero de hosts por redes
        num_host = CalculateIP.totalHostRede(conv_bits_mask, cl_rede)
        self.ui.label_host_value.setText(str(num_host))
        
        #Numero de rede de grupos hosts
        num_rede = CalculateIP.totalRede(conv_bits_mask, cl_rede)
        self.ui.label_subrede_value.setText(str(num_rede))

        #Total de bits para hosts 
        total_bits_host = CalculateIP.totalBitsHost(conv_bits_mask)
        self.ui.label_bitshost_value.setText(str(total_bits_host))

        #Total de bits para rede 
        total_bits_rede = CalculateIP.totalBitsRede(conv_bits_mask)
        self.ui.label_bitsredes_value.setText(str(total_bits_rede))

        #Indice de variação de rede
        variation_index = CalculateIP.variationIndex(num_host)
        self.ui.label_variationindex_value.setText(str(variation_index))

        #Ips úteis
        self.ui.label_userfulip_value.setText(str(num_host - 2))
        #Redes úteis
        self.ui.label_userfulsub_value.setText(str(num_rede - 2))

    def buttonClear(self):
        self.ui.lineEdit_rede.setText('')
        self.ui.lineEdit_mask.setText('')
        self.ui.lineEdit_gateway.setText('')

    