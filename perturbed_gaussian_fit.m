clear all
close all

% load tiff image
var_im=imread('Step065.tif');
% figure; 
% imshow(var_im);
% zoom on the interesting region
index1=400:1:500;
index2=1200:1:1300;
% show the interesting region
figure
imshow(var_im(index1,index2));
title('original tiff image');
var_int=rgb2gray(var_im);
% size(var_int)
var_rea=double(var_int(index1,index2));
% figure
% mesh(var_rea)
% grid on

image=var_rea;
% measure the curve parameters: mean values, variances, correlations, scale
% factor
pdfxy=image/sum(sum(image));
pdfx=sum(pdfxy);
pdfy=sum(pdfxy,2);
dx=1;
dy=1;
[Ny Nx]=size(image);
x=(1:Nx);
y=(1:Ny);
mx_meas=sum(x.*pdfx);
my_meas=sum(y'.*pdfy);
varx_meas=sum((x-mx_meas).^2.*pdfx);
vary_meas=sum((y-my_meas)'.^2.*pdfy);
cxy_meas=sum(sum(((y-my_meas)'*(x-mx_meas)).*pdfxy))/sqrt(varx_meas*vary_meas);
A_meas=max(max(image))/(2*pi*sqrt(varx_meas*vary_meas*(1-cxy_meas^2)));

figure
mesh(x,y,image);
grid on
title('original intensity');

% evaluate the gaussian fit
[curve3Dtmp] = gaussian3D(dx,dy,Nx,Ny,mx_meas,my_meas,varx_meas,vary_meas,cxy_meas,x,y);
curve3Dfit=A_meas*curve3Dtmp;
figure
mesh(x,y,curve3Dfit);
grid on
title('3D gaussian fit');

% parameters range is determined
Nsearch=5; % number of points use in search for each parameter
Xmin=mx_meas-sqrt(varx_meas)/3; Xmax=mx_meas+sqrt(varx_meas)/3;
Ymin=my_meas-sqrt(vary_meas)/3; Ymax=my_meas+sqrt(vary_meas)/3;
mx_vec=linspace(Xmin,Xmax,Nsearch);
my_vec=linspace(Ymin,Ymax,Nsearch);
varx_vec=linspace(0.2*varx_meas,1.3*varx_meas,Nsearch);
vary_vec=linspace(0.2*vary_meas,1.3*vary_meas,Nsearch);
if cxy_meas<0
    cmin=max(1.2*cxy_meas,-1);
    cmax=-cmin;
else
    cmax=min(1.2*cxy_meas,1);
    cmin=-cmax;
end
cxy_vec=linspace(cmin,cmax,9);
A_vec=linspace(0.8*A_meas,2.5*A_meas,Nsearch);
etot=[];
param=[];

% the solution is perturbed to achieve minimal error
for i1=1:length(mx_vec)
    mx=mx_vec(i1);
    for i2=1:length(my_vec)
        my=my_vec(i2);
        for i3=1:length(varx_vec)
            varx=varx_vec(i3);
            for i4=1:length(vary_vec)
                vary=vary_vec(i4);
                for i5=1:length(cxy_vec)
                    cxy=cxy_vec(i5);
                    for i6=1:length(A_vec)
                         A=A_vec(i6);
                         [curve3D] = gaussian3D(dx,dy,Nx,Ny,mx,my,varx,vary,cxy,x,y);
                         error=norm(A*curve3D-image);
                         etot=[etot error];
                         param=[param; mx my varx vary cxy A];
                    end
                end
            end
        end
    end
    i1
end

% minimum value of parameters
par_min=[Xmin Ymin 0.2*varx_meas 0.2*vary_meas cmin 0.8*A_meas]

[min_val min_ind]=min(etot);
% optimal parameters
param(min_ind,:)

% maximum value of parameters
par_max=[Xmax Ymax 1.3*varx_meas 1.3*vary_meas cmax 2.5*A_meas]

% minimal error
min_val
% normalized error energy
percent_error=100*(min_val/norm(image))

figure
plot(etot);
grid on
title('approximation error');

mx=param(min_ind,1); 
my=param(min_ind,2); 
varx=param(min_ind,3); 
vary=param(min_ind,4); 
cxy=param(min_ind,5);
A=param(min_ind,6);
% best approximation
[curve3Dtmp] = gaussian3D(dx,dy,Nx,Ny,mx,my,varx,vary,cxy,x,y);
curve_best=A*curve3Dtmp;

figure
mesh(x,y,curve_best);
grid on
hold on
mesh(x+Nx,y,curve_best-image);
title('perturbed gaussian approximation (L) and error (R)');
%  

