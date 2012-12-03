function gg=pipi(y)

    z=(size(y));
    if z(1,1)==2 then
        y=y';
    end
    dog = max(z);
    for k = 1:dog;
        n(k,1) = (y(k,1)-2*pi*(round(y(k,1)/2/pi)));
        n(k,2)=y(k,2);
    end
    gg=n;