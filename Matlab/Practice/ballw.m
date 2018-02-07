function f=ballw(K,ki)
% ballw.m 演示红色小球沿一条封闭螺线运动的实时动画
% 仅演示实时动画的调用格式为 ballw(K)
% 既演示实时动画又拍摄照片的调用格式为 f=ballw(K,ki)
% K 红球运动的循环数(不小于 1 )
% ki 指定拍摄照片的瞬间，取 1 到 1034 间的任意整数。
% f 存储拍摄的照片数据，可用 image(f.cdata) 观察照片。
% 产生封闭的运动轨线
t1=(0:1000)/1000*10*pi;x1=cos(t1);y1=sin(t1);z1=-t1;
t2=(0:10)/10;x2=x1(end)*(1-t2);y2=y1(end)*(1-t2);z2=z1(end)*ones(size(x2));
t3=t2;z3=(1-t3)*z1(end);x3=zeros(size(z3));y3=x3;
t4=t2;x4=t4;y4=zeros(size(x4));z4=y4;
x=[x1 x2 x3 x4];y=[y1 y2 y3 y4];z=[z1 z2 z3 z4];
%data=[x',y',z'];
h=plot3(x,y,z, 'y','Linewidth',2 ); axis off % 绘制曲线
% 定义 " 线 " 色、 " 点 " 型(点)、点的大小( 40 )、擦除方式( xor)
h=line( 'Color' ,[0.67 0 1], 'Marker' , '.' , 'MarkerSize' ,40, 'EraseMode' , 'xor' );
% 使小球运动
n=length(x);i=1;j=1;
while 1 % 无穷循环
    set(h, 'xdata' ,x(i), 'ydata' ,y(i), 'zdata' ,z(i));
    %bw=[x(i),y(i),z(i)]% 小球位置
    drawnow; % 刷新屏幕 <21>
    pause(0.0005) % 控制球速 <22>
    i=i+1;
    if nargin==2 && nargout==1 % 仅当输入宗量为 2 、输出宗量为 1 时，才拍摄照片
        if (i==ki&&j==1);f=getframe(gcf); end % 拍摄 i=ki 时的照片 <25>
    end
    if i>n
        i=1;j=j+1;
        if j>K; break ; end
    end
end
