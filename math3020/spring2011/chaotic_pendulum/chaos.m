function kk=chaos(initial1,initial2,timespan,timemap,speed,filename)
%initial1 = initial conditions of the first pendulum in the form of [theta,
%omega]
%initial2 = initial conditions of the second pendulum in the form of [theta,
%omega]
%timespan = maximum time to be evaluated at = scalar number
%timemap = spacing between "snapshots" in extended phase space
%speed = frames per second for the output movie
%filename = the name of the output file with extension .avi  i.e. example.avi

kk=filename;
init1=initial1;
init2=initial2;
time=[0 timespan];
option=odeset('MaxStep',(time(2)-time(1))/1000);
[t1,y1]=ode45(@cps,time,init1,option);
[t2,y2]=ode45(@cps,time,init2,option);

time_space=0:timemap:time(2);

y2_spacei = interp1(t2,y2(:,1),time_space,'linear');
y1_spacei = interp1(t1,y1(:,1),time_space,'linear');

v1_space = interp1(t1,y1(:,2),time_space,'linear');
v2_space = interp1(t2,y2(:,2),time_space,'linear');

y1_space=pipi([y1_spacei',v1_space']);
y2_space=pipi([y2_spacei',v2_space']);

ax_lim = ceil(max([v1_space,v2_space,-v1_space,-v2_space]));
figure(1);hold;grid;axis([-pi pi -ax_lim ax_lim]);
for k=1:max(size(time_space))

plot(y1_space(k,1),y1_space(k,2),'.g',y2_space(k,1),y2_space(k,2),'.b');
xlabel('\theta (rad)','Fontsize',16)
ylabel('\omega (rad/s)','Fontsize',16)
title('\it{\bf{Two Chaotic Pendulums}}','Fontsize',16)
 H(k)=getframe;  
 W(k)=getframe(gcf);
end
    movie(H,1,speed)
movie2avi(W,'filename','compression','None','fps',speed)
end

