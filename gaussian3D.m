function [ curve3D] = gaussian3D(dx,dy,Nx,Ny,mx,my,sigma2x,sigma2y,cxy,x,y )
% this subroutine generates a correlated Gaussian in 3D with given parameters
% 
% x=linspace(0,(Nx-1)*dx,Nx);
% y=linspace(0,(Ny-1)*dy,Ny)';
C1=2*pi*sqrt(sigma2x*sigma2y*(1-cxy^2));
Ax=ones(Ny,1)*((x-mx).^2/sigma2x);
Ay=(((y-my)').^2/sigma2y)*ones(1,Nx);
Axy=-2*cxy*((y-my)')*(x-mx)/sqrt(sigma2x*sigma2y);
C2=-0.5/(1-cxy^2);
Atot=C2*(Ax+Ay+Axy);
curve3D=C1*exp(Atot);
end

