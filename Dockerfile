FROM dev.passer.zyheal.com:8087/zyheal/pdf-server:v0.2.0

COPY pdf_server/ /app/pdf_server/
# 切换到pdfServer用户, 因为pipenv环境在pdfServer用户下
USER pdfServer 
ENTRYPOINT ["/app/pdf_server/pro-run.sh"]