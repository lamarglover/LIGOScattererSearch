Amp = 5000
mu_x = 2400
mu_y = 2400
sigma_x = 50
sigma_y = 50

gauss_guess = [Amp,mu_x,mu_y,sigma_x,sigma_y]
x = gauss_guess

b = reshape(Scatterers0206, [1, size(Scatterers0206)]);
xdata = b

function F = D2GaussFunction(x,xdata)
 F = x(1)*exp(   -((xdata(:,:,1)-x(2)).^2/(2*x(3)^2) + (xdata(:,:,2)-x(4)).^2/(2*x(5)^2) )    );
 
3Dplot(xdata) 