@echo off
setlocal

cd /d "%~dp0"

echo Gerando HTML do site Quarto em docs...
quarto render

if errorlevel 1 (
  echo.
  echo Falha ao gerar o site.
  exit /b 1
)

echo.
echo Site gerado com sucesso em docs\index.html
exit /b 0
