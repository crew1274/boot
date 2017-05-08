#電表最大數量
hxDEVICE_METER_MAX = 72
hxDEVICE_LT_MAX = 64

#電表資料通訊位址，請參考CC2030-通訊位址資料表
adMETER_DATA_BEGIN_H = 0x60
adMETER_DATA_BEGIN_L = 0
# 56種電力資訊
adMETER_DATA_TYPES_LENGTH = 56

#電表資料記憶體位址
#unsigned char dbMETER_DATA_BUFF[adMETER_DATA_END]
#程式如下：
#void RUN_PC_READ_METER_DATA()
#void RUN_WRITE_DATA()
adMETER_R_V_BEGIN = 0
adMETER_S_V_BEGIN = (adMETER_R_V_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_V_BEGIN = (adMETER_S_V_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_RS_V_BEGIN = (adMETER_T_V_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_ST_V_BEGIN = (adMETER_RS_V_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_TR_V_BEGIN = (adMETER_ST_V_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_I_BEGIN = (adMETER_TR_V_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_I_BEGIN = (adMETER_R_I_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_I_BEGIN = (adMETER_S_I_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_AVERAGE_I_BEGIN = (adMETER_T_I_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_P_BEGIN = (adMETER_AVERAGE_I_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_P_BEGIN = (adMETER_R_P_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_P_BEGIN = (adMETER_S_P_BEGIN + (hxDEVICE_METER_MAX * 4)) 
adMETER_ALL_P_BEGIN = (adMETER_T_P_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_Q_BEGIN = (adMETER_ALL_P_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_Q_BEGIN = (adMETER_R_Q_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_Q_BEGIN = (adMETER_S_Q_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_ALL_Q_BEGIN = (adMETER_T_Q_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_S_BEGIN = (adMETER_ALL_Q_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_S_BEGIN = (adMETER_R_S_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_S_BEGIN = (adMETER_S_S_BEGIN + (hxDEVICE_METER_MAX * 4)) 
adMETER_ALL_S_BEGIN = (adMETER_T_S_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_EP_BEGIN = (adMETER_ALL_S_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_EP_BEGIN = (adMETER_R_EP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_EP_BEGIN = (adMETER_S_EP_BEGIN + (hxDEVICE_METER_MAX * 4)) 
adMETER_ALL_EP_BEGIN = (adMETER_T_EP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_PEAK_R_EP_BEGIN = (adMETER_ALL_EP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_PEAK_S_EP_BEGIN = (adMETER_PEAK_R_EP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_PEAK_T_EP_BEGIN = (adMETER_PEAK_S_EP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_PEAK_ALL_EP_BEGIN = (adMETER_PEAK_T_EP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_EQ_BEGIN = (adMETER_PEAK_ALL_EP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_EQ_BEGIN = (adMETER_R_EQ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_EQ_BEGIN = (adMETER_S_EQ_BEGIN + (hxDEVICE_METER_MAX * 4)) 
adMETER_ALL_EQ_BEGIN = (adMETER_T_EQ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_01_MIN_DEMAND = (adMETER_ALL_EQ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_15_MIN_DEMAND = (adMETER_01_MIN_DEMAND + (hxDEVICE_METER_MAX * 4))
adMETER_R_GEP_BEGIN = (adMETER_15_MIN_DEMAND + (hxDEVICE_METER_MAX * 4))
adMETER_S_GEP_BEGIN = (adMETER_R_GEP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_GEP_BEGIN = (adMETER_S_GEP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_ALL_GEP_BEGIN = (adMETER_T_GEP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_GEQ_BEGIN = (adMETER_ALL_GEP_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_GEQ_BEGIN = (adMETER_R_GEQ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_GEQ_BEGIN = (adMETER_S_GEQ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_ALL_GEQ_BEGIN = (adMETER_T_GEQ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_PF_BEGIN = (adMETER_ALL_GEQ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_PF_BEGIN = (adMETER_R_PF_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_PF_BEGIN = (adMETER_S_PF_BEGIN + (hxDEVICE_METER_MAX * 4)) 
adMETER_ALL_PF_BEGIN = (adMETER_T_PF_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_HZ_BEGIN = (adMETER_ALL_PF_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_PW_BEGIN = (adMETER_HZ_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_PT_BEGIN = (adMETER_PW_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_R_CT_BEGIN = (adMETER_PT_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_S_CT_BEGIN = (adMETER_R_CT_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_T_CT_BEGIN = (adMETER_S_CT_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_DI_BEGIN = (adMETER_T_CT_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_DO_BEGIN = (adMETER_DI_BEGIN + (hxDEVICE_METER_MAX * 4))
adMETER_DATA_END = (adMETER_DO_BEGIN + (hxDEVICE_METER_MAX * 4))

#METER_ALL_DATA_BUFF = [0] * adMETER_DATA_END
METER_ALL_DATA_BUFF = []

#電表設定通訊位址，請參考CC2030-通訊設定表
adDEVICE_DATA_BEGIN_H = 0xA0
adDEVICE_DATA_BEGIN_L = 0

#電表設定記憶體位址
#unsigned char dbDEVICE_DATA_BUFF[adDEVICE_SETUP_END]
#程式如下：
#void RUN_PC_READ_DEVICE_DATA()
#void RUN_PC_WRITE_DEVICE_DATA()
adMETER_DEVICE_BEGIN = (0)
adLIGHT_DEVICE_BEGIN = (adMETER_DEVICE_BEGIN + (hxDEVICE_METER_MAX * 6))
adRTC_BEGIN = (adLIGHT_DEVICE_BEGIN + (hxDEVICE_LT_MAX * 4))
adDEVICE_WORK_BEGIN = (adRTC_BEGIN + 8)
adWRITE_BUFF_USED_BEGIN = (adDEVICE_WORK_BEGIN + 10)
adDEVICE_SETUP_END = (adWRITE_BUFF_USED_BEGIN + 2)


#無設備代碼，請參考CC2030-通訊設定表
hxNONE_DEVICE = 0

#電度表設備代碼表，請參考CC2030-通訊設定表
hxDEVICE_KWH_METER_BEGIN = (0x0300+0)
hxDEVICE_ACUVIM = (0x0300+0)
hxDEVICE_DEM320 = (0x0300+1)
hxDEVICE_DEM330 = (0x0300+2)
hxDEVICE_DEM510C = (0x0300+3)
hxDEVICE_DEM510C_0 = (0x0300+4)
hxDEVICE_DEM510C_1P = (0x0300+5)
hxDEVICE_DEM510C_2 = (0x0300+6)
hxDEVICE_DEM510C_2RS = (0x0300+7)
hxDEVICE_DEM510C_3 = (0x0300+8)
hxDEVICE_DEM510C_AB = (0x0300+9)
hxDEVICE_DEM510C_RS232_1_2 = (0x0300+10)
hxDEVICE_DEM510F_5 = (0x0300+11)
hxDEVICE_DEM510M_1P = (0x0300+12)
hxDEVICE_DEM520_1_2 = (0x0300+13)
hxDEVICE_DEM530C = (0x0300+14)
hxDEVICE_DEM530D = (0x0300+15)
hxDEVICE_DEM530D_3 = (0x0300+16)
hxDEVICE_DEM530D_3_2RS = (0x0300+17)
hxDEVICE_DEM530D_3_2RS_1_3 = (0x0300+18)
hxDEVICE_DEM530M = (0x0300+19)
hxDEVICE_DEM540C_1P = (0x0300+20)
hxDEVICE_DEM540C_1P_S = (0x0300+21)
hxDEVICE_DEM540C_2 = (0x0300+22)
hxDEVICE_DEM540C_2RS = (0x0300+23)
hxDEVICE_DEM540C_3 = (0x0300+24)
hxDEVICE_DEM540C_Q20 = (0x0300+25)
hxDEVICE_DEM550_5 = (0x0300+26)
hxDEVICE_DEM550_R = (0x0300+27)
hxDEVICE_DEM560D = (0x0300+28)
hxDEVICE_DEM560D_3 = (0x0300+29)
hxDEVICE_DEM560D_3_3 = (0x0300+30)
hxDEVICE_DEM560D_3_2RS_3_3 = (0x0300+31)
hxDEVICE_DEM560M_1_3 = (0x0300+32)
hxDEVICE_DEM560M_3_3 = (0x0300+33)
hxDEVICE_DEM570 = (0x0300+34)
hxDEVICE_DEM600D_1P_3_3 = (0x0300+35)
hxDEVICE_DEM600D_1P_3_4 = (0x0300+36)
hxDEVICE_DEM600D_2_3_3 = (0x0300+37)
hxDEVICE_DEM600D_2_3_4 = (0x0300+38)
hxDEVICE_DEM600D_3_4 = (0x0300+39)
hxDEVICE_DEM600D_3_2RS_3_3 = (0x0300+40)
hxDEVICE_DEM600D_3_2RS_3_4 = (0x0300+41)
hxDEVICE_DEM600D_3_2RS_DO_3_3 = (0x0300+42)
hxDEVICE_DEM600D_3_2RS_DO_3_4 = (0x0300+43)
hxDEVICE_DEM600D_3_2RS_DO_NC_3_3 = (0x0300+44)
hxDEVICE_DEM600D_3_3_3 = (0x0300+45)
hxDEVICE_DEM600D_3_3_4 = (0x0300+46)
hxDEVICE_DEM600D_3_DO_3_3 = (0x0300+47)
hxDEVICE_DEM600D_4_3_3 = (0x0300+48)
hxDEVICE_DEM600D_4_3_4 = (0x0300+49)
hxDEVICE_DEM600D_5_3_4 = (0x0300+50)
hxDEVICE_DEM600D_5P_3_4 = (0x0300+51)
hxDEVICE_DEM600D_7_3_4 = (0x0300+52)
hxDEVICE_DEM720_1_1p2w = (0x0300+53)
hxDEVICE_DEM720_2_1p2w = (0x0300+54)
hxDEVICE_DEM730 = (0x0300+55)
hxDEVICE_DEM740 = (0x0300+56)
hxDEVICE_DEM750 = (0x0300+57)
hxDEVICE_DFM630_2_3_4 = (0x0300+58)
hxDEVICE_EPM420 = (0x0300+59)
hxDEVICE_EPM420_5S_3_4 = (0x0300+60)
hxDEVICE_EPM420P_110V = (0x0300+61)
hxDEVICE_EPM420_Q015 = (0x0300+62)
hxDEVICE_ESmeter_120_1P2W = (0x0300+63)
hxDEVICE_ESmeter_340_3P4W = (0x0300+64)
hxDEVICE_ESmeter_345_3P4W = (0x0300+65)
hxDEVICE_KWH_METER_MAX = (0x0300+66)

#多功能電表代碼表，請參考CC2030-通訊設定表
hxDEVICE_FUNC_METER_BEGIN = (0x0400+0)
hxDEVICE_PM100 = (0x0400+0)
hxDEVICE_PM200_A = (0x0400+1)
hxDEVICE_PM200_B = (0x0400+2)
hxDEVICE_PM200_C = (0x0400+3)
hxDEVICE_PM200_STD = (0x0400+4)
hxDEVICE_PM210_4_A = (0x0400+5)
hxDEVICE_PM210_4_B = (0x0400+6)
hxDEVICE_PM210_4_C = (0x0400+7)
hxDEVICE_PM210_4_STD = (0x0400+8)
hxDEVICE_PM210_A = (0x0400+9)
hxDEVICE_PM210_B = (0x0400+10)
hxDEVICE_PM210_C = (0x0400+11)
hxDEVICE_PM210_P_A = (0x0400+12)
hxDEVICE_PM210_P_B = (0x0400+13)
hxDEVICE_PM210_P_C = (0x0400+14)
hxDEVICE_PM210_P_STD = (0x0400+15)
hxDEVICE_PM210_STD = (0x0400+16)
hxDEVICE_PM210_X_A = (0x0400+17)
hxDEVICE_PM210_X_B = (0x0400+18)
hxDEVICE_PM210_X_C = (0x0400+19)
hxDEVICE_PM210_X_STD = (0x0400+20)
hxDEVICE_PM250_4_A = (0x0400+21)
hxDEVICE_PM250_4_B = (0x0400+22)
hxDEVICE_PM250_4_C = (0x0400+23)
hxDEVICE_PM250_4_STD = (0x0400+24)
hxDEVICE_PM250_4_PROJECT = (0x0400+25)
hxDEVICE_PM250_S_A = (0x0400+26)
hxDEVICE_PM250_S_B = (0x0400+27)
hxDEVICE_PM250_S_C = (0x0400+28)
hxDEVICE_PM250_S_STD = (0x0400+29)
hxDEVICE_PM250_S_PROJECT = (0x0400+30)
hxDEVICE_PM250_X_A = (0x0400+31)
hxDEVICE_PM250_X_B = (0x0400+32)
hxDEVICE_PM250_X_C = (0x0400+33)
hxDEVICE_PM250_X_STD = (0x0400+34)
hxDEVICE_PM250_X_PROJECT = (0x0400+35)
hxDEVICE_PME_1130 = (0x0400+36)
hxDEVICE_PME_1210 = (0x0400+37)
hxDEVICE_PME_1230 = (0x0400+38)
hxDEVICE_POLARIS_120_A = (0x0400+39)
hxDEVICE_POLARIS_120_B = (0x0400+40)
hxDEVICE_POLARIS_120_C = (0x0400+41)
hxDEVICE_POLARIS_240_A = (0x0400+42)
hxDEVICE_POLARIS_240_B = (0x0400+43)
hxDEVICE_POLARIS_240_C = (0x0400+44)
hxDEVICE_POLARIS_P103 = (0x0400+45)
hxDEVICE_POLARIS_P153 = (0x0400+46)
hxDEVICE_POLARIS_P202 = (0x0400+47)
hxDEVICE_POLARIS_P204 = (0x0400+48)
hxDEVICE_POLARIS_P205 = (0x0400+49)
hxDEVICE_POLARIS_P206 = (0x0400+50)
hxDEVICE_POLARIS_P252 = (0x0400+51)
hxDEVICE_POLARIS_P254 = (0x0400+52)
hxDEVICE_POLARIS_P255 = (0x0400+53)
hxDEVICE_POLARIS_P256 = (0x0400+54)
hxDEVICE_POLARIS_P302 = (0x0400+55)
hxDEVICE_POLARIS_P304 = (0x0400+56)
hxDEVICE_POLARIS_P305 = (0x0400+57)
hxDEVICE_POLARIS_P306 = (0x0400+58)
hxDEVICE_SMB350_4_A = (0x0400+59)
hxDEVICE_SMB350_4_B = (0x0400+60)
hxDEVICE_SMB350_4_C = (0x0400+61)
hxDEVICE_SMB350_8_A = (0x0400+62)
hxDEVICE_SMB350_8_B = (0x0400+63)
hxDEVICE_SMB350_8_C = (0x0400+64)
hxDEVICE_SMB350_8_S = (0x0400+65)
hxDEVICE_SMB350_8_PROJECT = (0x0400+66)
hxDEVICE_FUNC_METER_MAX = (0x0400+67)

#設備有重覆位址，目前僅用於SMB350
hxDEVICE_DUPLICATE_ADDR = (0x8000)

#寫入資料型態，請參考CC2030-通訊位址資料表
hxWRITE_R_EP = 1
hxWRITE_S_EP = 2
hxWRITE_T_EP = 3
hxWRITE_ALL_EP = 4
hxWRITE_R_EQ = 5
hxWRITE_S_EQ = 6
hxWRITE_T_EQ = 7
hxWRITE_ALL_EQ = 8
hxWRITE_R_GEP = 9
hxWRITE_S_GEP = 10
hxWRITE_T_GEP = 11
hxWRITE_ALL_GEP = 12
hxWRITE_R_GEQ = 13
hxWRITE_S_GEQ = 14
hxWRITE_T_GEQ = 15
hxWRITE_ALL_GEQ = 16
hxWRITE_METER_PW = 17
hxWRITE_METER_PT = 18
hxWRITE_METER_CT = 19
hxWRITE_METER_DO = 20

#讀取電表長度不可超過51 WORDS
#每次讀取長度不同，以長度判斷資料內容
hxPM210_DATA_LENGTH_1 = 40
hxPM210_DATA_LENGTH_2 = 44
hxPM210_DATA_LENGTH_3 = 32

hxSMB350_RST_V_LENGTH = 12
hxSMB350_CH0104_RST_I_LENGTH = 25
hxSMB350_CH0508_RST_I_LENGTH = 27
hxSMB350_CH0104_RST_P_LENGTH = 29
hxSMB350_CH0508_RST_P_LENGTH = 30
hxSMB350_CH0104_RST_EP_LENGTH = 31
hxSMB350_CH0508_RST_EP_LENGTH = 32
hxSMB350_CH0104_RST_EQ_LENGTH = 33
hxSMB350_CH0508_RST_EQ_LENGTH = 34
hxSMB350_CH0104_RST_PF_LENGTH = 13
hxSMB350_CH0508_RST_PF_LENGTH = 14
hxSMB350_CH0102_ALL_LENGTH = 35
hxSMB350_CH0304_ALL_LENGTH = 36
hxSMB350_CH0506_ALL_LENGTH = 37
hxSMB350_CH0708_ALL_LENGTH = 38
hxSMB350_HZ_LENGTH = 1
hxSMB350_CT_LENGTH = 24
hxSMB350_CH0104_RST_PEAK_EP_LENGTH = 26
hxSMB350_CH0508_RST_PEAK_EP_LENGTH = 28
hxSMB350_ALL_PEAK_EP_LENGTH = 16

hxMETER_1P2W = 0
hxMETER_1P3W = 1
hxMETER_3P3W_2CT = 2
hxMETER_3P3W_3CT = 3
hxMETER_3P4W = 4

hxSMB350_COMPARE_ADDR = 0
hxSMB350_EXIST = 1

hxWRITE_DEVICE_ADDR = 0
hxWRITE_DEVICE_DATA_ADDR_H = 1
hxWRITE_DEVICE_DATA_ADDR_L = 2
hxWRITE_DEVICE_DATA_HH = 3
hxWRITE_DEVICE_DATA_HL = 4
hxWRITE_DEVICE_DATA_LH = 5
hxWRITE_DEVICE_DATA_LL = 6
hxWRITE_DEVICE_BAUD_RATE = 7
hxWRITE_DEVICE_DATA_MAX = 8

hxWRITE_SMB350_R_EP_MODE = 0
hxWRITE_SMB350_S_EP_MODE = 1
hxWRITE_SMB350_T_EP_MODE = 2
hxWRITE_PM210_ALL_EP_MODE = 3
hxWRITE_SMB350_R_EQ_MODE = 4
hxWRITE_SMB350_S_EQ_MODE = 5
hxWRITE_SMB350_T_EQ_MODE = 6
hxWRITE_PM210_ALL_EQ_MODE = 7
hxWRITE_PM210_ALL_GEP_MODE = 8
hxWRITE_PM210_ALL_GEQ_MODE = 9
hxWRITE_PM210_PW_MODE = 10
hxWRITE_METER_PT_MODE = 11
hxWRITE_METER_R_CT_MODE = 12
hxWRITE_METER_S_CT_MODE = 13
hxWRITE_METER_T_CT_MODE = 14
hxWRITE_METER_DO_MODE = 15

#CH
METER_CH_MAX = 8
