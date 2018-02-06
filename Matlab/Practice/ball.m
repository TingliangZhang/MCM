Ball.m
%Script file ball.m
%
%Purpose:
%  This program calculates the distance traveled by a ball
%throw at a speciified angle "theta" and a specified velocity
%"vo" from a point,ignoring air friction.It calculates the angle
%yeileding maximun range,and also plots selected trajectories.
%
%Define variable:
%conv       degrees to radians conv factor
%grav       The gravity accel
%ii,jj      Loop index
%index      The maximum range in array
%maxangle   The angle that gives the maximum range
%maxrange   Maximum range
%range      ranghe for a specified angle
%time       Time
%theta      Inital angle
%fly_time   the totle trajectory time
%vo         The initial velocity
%vxo        x-component of the initial velocity
%vyo        y-component of the initial velocity
%x          x-position of ball
%y          y-position of ball
%定义常数数值
conv=pi/180;
grav=-9.82;
vo=input('Enter the initial velocity:');
 
range=zeros(1,91);
 %计算最大的水平距离
for ii=1:91
    theta =ii-1;
    vxo=vo*cos(theta*conv);
    vyo=vo*sin(theta*conv);
    max_time=-2*vyo/grav;
    range(ii)=vxo*max_time;
end
%显示计算水平距离的列表 
fprintf('Range versus angle theta"\n');
for ii=1:5:91
    theta=ii-1;
    fprintf('%2d %8.4f\n',theta,range(ii));
end
%计算最大的角度和水平距离 
[maxrange index]=max(range);
maxangle = index-1;
fprintf('\n Max range is %8.4f at %2d degress.\n',maxrange,maxangle);
%绘制轨迹图形 
for ii=5:10:80
    theta=ii;
    vxo=vo*cos(theta*conv);
    vyo=vo*sin(theta*conv);
    max_time=-2*vyo/grav;
    %计算小球轨迹的x,y坐标数值
    x=zeros(1,21);
    y=zeros(1,21);
    for jj=1:21
        time=(jj-1)*max_time/20;
        x(jj)=vxo*time;
        y(jj)=vyo*time+0.5*grav*time^2;
    end
    plot(x,y,'g');
    if ii==5
        hold on;
    end
end
    %添加图形的标题和坐标轴名称
    title('\bf Trajectory of Ball vs Inital Angle\theta');
    xlabel('\bf\itx \rm\bf(meters)');
    ylabel('\bf\ity \rm\bf(meters)');
    axis([0 max(range)+5 0 -vo^2/2/grav]);
    grid on;
    %绘制最大水平的轨迹图形
    vxo=vo*cos(maxangle*conv);
    vyo=vo*sin(maxangle*conv);
    max_time=-2*vyo/grav;
        %Calculate the (x,y)
        x=zeros(1,21);
        y=zeros(1,21);
        for jj=1:21
            time=(jj-1)*max_time/20;
            x(jj)=vxo*time;
            y(jj)=vyo*time+0.5*grav*time^2;
        end
        plot(x,y,'r','Linewidth',2);
        hold off
