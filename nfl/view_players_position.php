<!DOCTYPE html>
<html lang="en">

<head>
  <title>Soccer &mdash; Website by Colorlib</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">


  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="fonts/icomoon/style.css">

  <link rel="stylesheet" href="css/bootstrap/bootstrap.css">
  <link rel="stylesheet" href="css/jquery-ui.css">
  <link rel="stylesheet" href="css/owl.carousel.min.css">
  <link rel="stylesheet" href="css/owl.theme.default.min.css">
  <link rel="stylesheet" href="css/owl.theme.default.min.css">

  <link rel="stylesheet" href="css/jquery.fancybox.min.css">

  <link rel="stylesheet" href="css/bootstrap-datepicker.css">

  <link rel="stylesheet" href="fonts/flaticon/font/flaticon.css">

  <link rel="stylesheet" href="css/aos.css">

  <link rel="stylesheet" href="css/style.css">

  <style>
    /* CSS for the hamburger menu and home button */
   .home-button {
      position: fixed;
      top: 20px;
      right: 20px; 
      z-index: 1000;
      color: #fff;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
    }

    /* Other styles */
  </style>

</head>

<body>

  <div class="site-wrap">

    <div class="site-mobile-menu site-navbar-target">
      <div class="site-mobile-menu-header">
        <div class="site-mobile-menu-close">
          <span class="icon-close2 js-menu-toggle"></span>
        </div>
      </div>
      <div class="site-mobile-menu-body"></div>
    </div>


    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Hamburger Menu</title>
      <style>
          /* CSS for the hamburger menu */
          .menu-icon {
              cursor: pointer;
              display: block;
              position: fixed;
              top: 20px;
              left: 20px;
              z-index: 1000;
          }
          .menu-icon span {
              display: block;
              width: 30px;
              height: 3px;
              background-color: #ffffff;
              margin: 5px 0;
          }
          .menu-icon.open span:nth-child(1) {
              transform: rotate(45deg) translate(5px, 5px);
          }
          .menu-icon.open span:nth-child(2) {
              opacity: 0;
          }
          .menu-icon.open span:nth-child(3) {
              transform: rotate(-45deg) translate(7px, -7px);
          }
          .menu {
              position: fixed;
              top: 0;
              left: -300px;
              width: 250px;
              height: 100%;
              background-color: #f4f4f4;
              z-index: 999;
              transition: left 0.3s ease-in-out;
          }
          .menu.open {
              left: 0;
          }
          .menu ul {
              list-style: none;
              padding: 0;
              margin: 50px 0 0 0;
          }
          .menu ul li {
              padding: 10px 20px;
              border-bottom: 1px solid #ccc;
          }
      </style>
      </head>
      <body>
        <a href="index.php" class="home-button">Home</a>
      <!-- Hamburger Icon -->
      <div class="menu-icon" onclick="toggleMenu()">
          <span></span>
          <span></span>
          <span></span>
      </div>
      
      <!-- Menu -->
    <div class="menu" id="menu">
        <ul>
            <li><a href="index.php">Home</a></li>
            <li><a href="add_game.php">New Game</a></li>
            <li><a href="new_player.php">New Player</a></li>
            <li><a href="view_team.php">View Team</a></li>
            <li><a href="view_players_position.php">View Players of a Position</a></li>
            <li><a href="view_all_teams.php">View All Teams</a></li>
            <li><a href="view_team_games.php">View All Games by a Team</a></li>
            <li><a href="view_games_date.php">View All Games on a Day</a></li>
        </ul>
    </div>

      <script>
          // JavaScript to toggle the menu
          function toggleMenu() {
              var menu = document.getElementById('menu');
              menu.classList.toggle('open');
          }
      </script>
      
      </body>

    <div class="hero overlay" style="background-image: url('images/football_bg.jpeg');">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-5 mx-auto text-center">
            <h1 class="text-white">View All Players of a Position</h1>
            <p>View all the players of a particular position with our intuitive site.</p>
          </div>
        </div>
      </div>
    </div>
    <h2>Player Information</h2>

    <?php
      $pos = escapeshellarg($_POST['playerPosition']);
      $command = 'python3 nfl.py view_players_position ' . $pos;
      $escaped_command = escapeshellcmd($command);
      // $output = shell_exec($command);
      system($escaped_command);
    ?>

    <form action="view_players_position.php" method="post">
        <div>
	<select class="form-control" name="playerPosition" id="playerPosition" required>
          <option value="" disabled selected>Select a position</option>
          <option value="Center">Defender</option>
          <option value="Offensive Guard">Offensive Guard</option>
          <option value="Offensive Tackle">Offensive Tackle</option>
          <option value="Quarterback">Quarterback</option>
          <option value="Running Back">Running Back</option>
          <option value="Wide Receiver">Wide Receiver</option>
          <option value="Defensive Tackle">Defensive Tackle</option>
          <option value="Nose Tackle">Nose Tackle</option>
          <option value="Defensive End">Defensive End</option>
          <option value="Middle Linebacker">Middle Linebacker</option>
          <option value="Outside Linebacker">Outside Linebacker</option>
          <option value="Cornerback">Cornerback</option>
        </select>
	</div>
        <button type="submit">Submit</button>
    </form>



      <div class="container">
            
            <div class="widget-next-match">
              <table class="table custom-table">
              </table>
            </div>
      </div>


    <footer class="footer-section">
      <div class="container">

        <div class="row text-center">
          <div class="col-md-12">
            <div class=" pt-5">
              <p>
                <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                Copyright &copy;
                <script>
                  document.write(new Date().getFullYear());
                </script> All rights reserved | This template is made with <i class="icon-heart"
                  aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
                <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
              </p>
            </div>
          </div>

        </div>
      </div>
    </footer>



  </div>
  <!-- .site-wrap -->

  <script src="js/jquery-3.3.1.min.js"></script>
  <script src="js/jquery-migrate-3.0.1.min.js"></script>
  <script src="js/jquery-ui.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/owl.carousel.min.js"></script>
  <script src="js/jquery.stellar.min.js"></script>
  <script src="js/jquery.countdown.min.js"></script>
  <script src="js/bootstrap-datepicker.min.js"></script>
  <script src="js/jquery.easing.1.3.js"></script>
  <script src="js/aos.js"></script>
  <script src="js/jquery.fancybox.min.js"></script>
  <script src="js/jquery.sticky.js"></script>
  <script src="js/jquery.mb.YTPlayer.min.js"></script>


  <script src="js/main.js"></script>

</body>

</html>
