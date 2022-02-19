#include <SPI.h>
#include <RFID.h>

#define SS_PIN 10
#define RST_PIN 9

RFID rfid(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.init();
}

void loop() {
  if (rfid.isCard()) {
    if (rfid.readCardSerial()) {
      for (int i = 0; i < sizeof(rfid.serNum); i++) {
        Serial.print(rfid.serNum[i], DEC);
      }
      Serial.println();
    }
  }
  rfid.halt();
}
