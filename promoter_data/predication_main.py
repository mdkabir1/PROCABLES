from prediction_promoter import prediction_promoter

# model_SW='9Lastepoch_new.h5'
# iput_data_SW='SW.txt'
model_promoter='7Lastepoch_new.h5'
iput_data_promoter='P-Non.txt'

# pred,prob= prediction_funct(iput_data,model_SW)
# print(pred)
pred, prob = prediction_promoter(iput_data_promoter, model_promoter)
print(pred)
