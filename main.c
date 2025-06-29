#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    FILE *fp = fopen("sensor_data.csv", "w");
    if (fp == NULL) {
        perror("Failed to open file");
        return 1;
    }
    fprintf(fp, "time,temperature,humidity,acceleration\n");
    srand((unsigned)time(NULL));
    for (int i = 0; i < 100; i++) {
        float temp = 20.0 + (rand() % 100) / 10.0;    // 20.0〜30.0℃
        float humi = 40.0 + (rand() % 500) / 10.0;    // 40.0〜90.0%
        float accel = (rand() % 2000 - 1000) / 100.0; // -10.0〜+10.0 m/s^2
        fprintf(fp, "%d,%.2f,%.2f,%.2f\n", i, temp, humi, accel);
    }
    fclose(fp);
    printf("Sensor data output successfully.\n");
    return 0;
}