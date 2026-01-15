# Generate Static PIX Code
- create virtual env
- install dependecies
- done

```
flask --app app run
```

http://127.0.0.1:5000/pix?txid=RANDOMCODE&value=1

## MUST BE changed inside .env file
.env.example included

- PKEY = Pix key
- PNAME = Merchant Name
- PCITY = Merchant City

## MUST BE include inside .cors file
.cors.example included

list with the allow hosts to access the app

## eg: Response
- 00020126250014br.gov.bcb.pix014TEST5204000053039865802BR5904TEST6004TEST62110507RP17273630472A1
