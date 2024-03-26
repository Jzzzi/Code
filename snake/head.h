#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
using namespace std;

struct point{
    int x;
    int y;
    void operator=(point p){
        x = p.x;
        y = p.y; 
    }
    bool operator==(point p){
        return x == p.x && y == p.y;
    }
    bool operator!=(point p){
        return x != p.x || y != p.y;
    }
};
typedef struct point point;

struct snake{
    private:
        int length;
        vector<point> body;
    public:
        snake(int xrange, int yrange){
            point p;
            srand((unsigned int)time(NULL));
            p.x = rand()%(xrange-1) + 1;
            p.y = rand()%(yrange-1) + 1;
            body.push_back(p);
            length = 1;
        }
        point gethead();
        int getlen();
        void move(int direction,point food);
        bool occupy(int x,int y);
        
};
typedef struct snake snake;

point snake::gethead(){
    return body[0];
}

int snake::getlen(){
    return length;
}

void snake::move(int direction,point food){
    point head = gethead();
    switch(direction){
        //0: up, 1: right, 2: down, 3: left
        case 0:
            head.y--;
            break;
        case 1:
            head.x++;
            break;
        case 2:
            head.y++;
            break;
        case 3:
            head.x--;
            break;
    }
    if(head!=food){
        for(int i = length - 1; i > 0; i--)
            body[i] = body[i-1];
        body[0] = head;
    }
    else if(head==food){
        body.push_back(body[length-1]);
        for(int i = length - 1; i > 0; i--)
            body[i] = body[i-1];
        body[0] = head;
        length++;
    }
}

bool snake::occupy(int x,int y){
    for(int i = 0;i < length;i++)
        if(x == body[i].x&&y == body[i].y)
            return true;
    return false;
}

point foodgen(int xrange,int yrange,snake snake){
    srand((unsigned int)time(NULL));
    point p;
    do{
        p.x = rand()%(xrange-1) + 1;
        p.y = rand()%(yrange-1) + 1;
    }while(snake.occupy(p.x,p.y));
    return p;
}

void display(int xrange,int yrange,snake snake,point food){
    for(int y = 0; y <= yrange; y++)
        for(int x = 0; x<=xrange; x++){
            if(x == xrange)
                printf("* \n");
            else if(x == 0||y == 0||y == yrange)
                printf("* ");
            else if(snake.occupy(x,y))
                printf("# ");
            else if(x == food.x&&y==food.y)
                printf("$ ");
            else
                printf("  ");
            }
}