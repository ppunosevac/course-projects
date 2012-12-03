function rr=cps(t,y)
    epsilon=.3;
    rr=[y(2); -sin(y(1))+epsilon*cos(t)];