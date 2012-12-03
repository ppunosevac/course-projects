%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% a program to simulate the logistic equation bifurcation chart for r =2 to 4   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%begin initialization of variables%
r_array = (2:0.0002:4)'; %sets the values for r and places them in a 10001X1 Array%
						 %(or vector)%
l = length(r_array);
iterations_per_r = 20;  %sets how many times the calculation will happen or how%
						 %many lines will be on the graph %
						 
y = zeros(length(r_array), iterations_per_r); %Preallocates the results matrix%

y0 = 0.5; %assigns the value for the initial value %

y(:,1) = r_array.*y0*(1-y0); % Assigns the initial value to the first row of results %

%end initialization of variables %

%begin calculations %

for i = 1:iterations_per_r-1  %begins calculation loop for however many cases assigned%
							  %in the variable iterations_per_r%
    y(:,i+1) = r_array.*y(:,i).*(1-y(:,i));
				%assigns the results calculation to the i+1 (2nd to 100th row of y %
				%Calculation takes the array and element wize multiplies it with   %
				%current row of Y then elementwise times the same row in 1-y       %
				
end			%ends the calculation loop when i=99 is finished%
%end calculations %
%begin plotting %
figure(1)
plot(r_array, y,'k-'); %plots columns of Y against the values in r_array,         %
					   %connects the points with a solid black line.              %
grid on; %turns on the grid background.
title('Bifurcation in the Logistics Equation')
xlabel('values of r')
ylabel('Population')

% begin calculations for exploring values of r  %
r=round(10000*r_array);   %take the values of r which have large roundoff errors          %
                          %and multiply them to get 6 digits to the left of the           %
                          %decimal point, then round them to the nearest whole number     %
r=r/10000;      %divide by 10000 to get 5 digits to the right of the decimal              %
%in the loop the values of r are used to pull out the index values for values of interest %
%These index values are then used to automate the plot labeling below                     %
%If more plots are desired, just add an if statement in the for block below for the value %
%in question assign it to a dummy variable of some sort (countXX) then add another figure %
%for it in the printing area below.                                                       %
for j=1:l;
    if r(j)==2.800
        count=j;
    end
    if r(j)==3.000
        count2=j;
    end
    if r(j)==3.400
        count3=j;
    end
    if r(j)==3.450
        count4=j;
    end
    if r(j)==3.810
        count5=j;
    end
    if r(j)==3.850
        count6=j;
    end
    if r(j)==3.950
        count7=j;
    end
    if r(j)==3.210
        count8=j;
    end
    if r(j)==3.500
        count9=j;
    end
    if r(j)==2.1
        count10=j;
    end
    
end
% calculations are done, now to start plotting  %
        
figure(2)
    plot (y(count,:))         %note count is the index for the r we want           %
    placeholder=r_array(count); %unlike MATLAB, FreeMAT doesn't like array         %
                                %elements in sprintf so I assign it to placeholder %
    s=sprintf('Logistic Result for R=%g',placeholder); %works fine with placeholer %
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

figure(3)   %figures 3 - end are copies of figure 2 with a different index holder  %
    plot (y(count2,:))
    placeholder=r_array(count2);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

figure(4)
    plot (y(count3,:))
    placeholder=r_array(count3);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

figure(5)
    plot (y(count4,:))
    placeholder=r_array(count4);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

figure(6)
    plot (y(count5,:))
    placeholder=r_array(count5);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

figure(7)
    plot (y(count6,:))
    placeholder=r_array(count6);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;
    
figure(8)
    plot (y(count7,:))
    placeholder=r_array(count7);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

 figure(9)
    plot (y(count8,:))
    placeholder=r_array(count8);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

figure(10)
    plot (y(count9,:))
    placeholder=r_array(count9);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;

figure(11)
    plot (y(count10,:))
    placeholder=r_array(count10);
    s=sprintf('Logistic Result for R=%g',placeholder);
    title(s)
    xlabel('Run Number')
    ylabel('value')
    grid on;




