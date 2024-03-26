#include "head.h"
int main()
{
    int xrange = 10;
    int yrange = 10;
    snake snake(xrange,yrange);
    point food = foodgen(xrange,yrange,snake);
    display(xrange,yrange,snake,food);
    snake.move(1,food);
    display(xrange,yrange,snake,food);
    return 0;
}
