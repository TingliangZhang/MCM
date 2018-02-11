a = [17425 , 52607 , 97507 ,122438 , 116099 , 158614 , 199826];
b = cumsum(a);
hold on;
grid on;
plot(a,'c-o');

x=1:7;
ylabel('EV num');
xlabel('Year');
plot(x,b,'r-*');

hold off;

set(gca,'xtick',[1:19]);
set(gca,'xticklabel',['2011';'2012';'2013';'2014';'2015';'2016';'2017'])

legend('Delta','Total');
