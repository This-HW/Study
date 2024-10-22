#!/usr/bin/env python3
import cgi
# 입력 양식의 글자 추출하기 --- (※1)
form = cgi.FieldStorage()

# 메인 처리 --- (※2)
def main():
    show_form()

# 입력 양식 출력하기 --- (※4)
def show_form():
    print("Content-Type: text/html; charset=euc-kr")
    print("")
    print("""
    <!DOCTYPE HTML>
<html>
<head>
  <link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
  <script src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
  <script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
 <script type="text/javascript">
    var xml;
    $(document).ready(function(){
      $.ajax({
        type: "GET",
        url: "../test.xml",
        dataType: "xml",
        success: xmlParser
      });
    });
        //loading XML file and parsing to .main div.
    function xmlParser(data) {
      xml = data;

      $(xml).find("Employee").each(function () {
          name = $(this).attr("name");
          var email = $(this).find("email").text();
          var jobtitle = $(this).find("jobtitle").text();
          var address = $(this).find("address").text();
          var workphone = $(this).find("workphone").text();
          var homephone = $(this).find("homephone").text();
          var cellphone = $(this).find("cellphone").text();
          var fax = $(this).find("fax").text();


          $("#list").append('<li><h3 id="name">' + name + '</h3><ul><li>Email: '+ email + '</li><li>Job Title: '+ jobtitle + '</li><li>Address: '+ address + '</li><li>Work Phone: '+ workphone + '</li><li>Home Phone: '+ homephone + '</li><li>Cell Phone: '+ cellphone + '</li><li>Fax: '+ fax + '</li></ul></li>');

      });

      $('#list').listview('refresh'); 

    }
  </script>
</head>
<body>
<div data-role="page">
  <div data-role="header" data-theme="a">
    <h1>Employees</h1>
  </div>
  <!-- /header -->
  <div data-role="content">
    <div class="content-primary">
      <ul id="list" data-role="listview" data-theme="a" data-filter="true">
      <li id="load">Loading Data...</li>
      </ul>
      <ul id="results" data-role="listview" data-theme="a">
      </ul>
    </div>
    <!-- /contentprimary --> 
  </div>
  <!-- /content -->
  <div data-role="footer" data-theme="a">
    <div data-role="navbar">
      <p align='center'>::: Footer :::</p>
    </div>
    <!-- /navbar --> 
  </div>
  <!-- /footer --> 
</div>
<!-- /page -->
</body>
</html>


    """)
main()