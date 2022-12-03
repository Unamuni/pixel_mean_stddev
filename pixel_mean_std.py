from PIL import Image
import numpy as np

import matplotlib.colors as clr
import matplotlib.pyplot as plt

# Update the matplotlib configuration parameters:
plt.rcParams.update({
                    'font.family': 'sans-serif',
                    'font.sans-serif': 'Helvetica',
                    'text.usetex': False,
#                     'lines.linewidth': 5,
                     'font.size': 22,
                     'xtick.direction': 'in',
                     'ytick.direction': 'in',
                     'xtick.labelsize': 'large',
                     'ytick.labelsize': 'large',
                     'axes.labelsize': 'medium',
                     'axes.titlesize': 'medium',
                     'axes.grid.axis': 'both',
                     'axes.grid.which': 'both',
                     'axes.grid': True,
                     'grid.color': 'xkcd:Charcoal',
                     'grid.alpha': 0.253,
                     'lines.markersize': 8,
                     'legend.borderpad': 0.2,
#                     'legend.fancybox': True,
                     'legend.fontsize': 'medium',
                     'legend.framealpha': 0.7,
                     'legend.handletextpad': 0.5,
                     'legend.labelspacing': 0.33,
                     'legend.loc': 'best',
                     'figure.figsize': (14, 10),
                     'savefig.dpi': 140,
                     'pdf.compression': 9})

fnames=[]
for ii in range(7):
    fnames.append(str(2**ii)+'.jpg')

ii_list  = []
mn_list  = []
var_list = []
std_list = []
    
i_start=501450
i_end=i_start+1000

fig, ax1 = plt.subplots(1)

for ii,fname in enumerate(fnames):
    img=Image.open(fname)
    img_ary=np.asarray(img)
    img_ary_flat=img_ary.flatten()
    r_ary=img_ary_flat[::3]
    g_ary=img_ary_flat[1::3]
    b_ary=img_ary_flat[2::3]

    ax1.plot(r_ary[i_start:i_end],'-',color=clr.hsv_to_rgb((ii/(len(fnames)),1,.9)),label='n='+fname[:-4])
    ax1.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
    ax1.set_xlabel('pixel')
    ax1.set_ylabel('value')
    
    n=len(b_ary[i_start:i_end])
    mn=np.mean(b_ary[i_start:i_end])
    var=np.sum((b_ary[i_start:i_end]-mn)**2)/(n-1)
    std=np.sqrt(var)
    print(ii,n,mn,var,std)

    ii_list.append(2**ii)
    mn_list.append(mn)
    var_list.append(var)
    std_list.append(std)

plt.savefig('./pixel.png', bbox_inches='tight')

fig, ax1 = plt.subplots(1)

ax1.loglog(ii_list, mn_list,'ro-',label='mean')
ax1.loglog(ii_list, std_list,'bo-',label='std_dev')
ax1.legend(loc='best')
ax1.set_xlabel('n')
ax1.set_ylabel('value')

plt.savefig('./mean_std.png', bbox_inches='tight')
