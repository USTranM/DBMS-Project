<!DOCTYPE html>
<html lang="en">

<head>
  <title>Add New Game Information</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">


  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="fonts/icomoon/style.css">

  <link rel="stylesheet" href="css/bootstrap.min.css">

  <link rel="stylesheet" href="css/bootstrap/bootstrap.css">
  <link rel="stylesheet" href="css/jquery-ui.css">
  <link rel="stylesheet" href="css/owl.carousel.min.css">
  <link rel="stylesheet" href="css/owl.theme.default.min.css">
  <link rel="stylesheet" href="css/owl.theme.default.min.css">

  <link rel="stylesheet" href="css/jquery.fancybox.min.css">


  <link rel="stylesheet" href="fonts/flaticon/font/flaticon.css">

  <link rel="stylesheet" href="css/aos.css">

  <link rel="stylesheet" href="css/style.css">

  <script>
      function validateForm() {
          var team1 = document.getElementById("team1").value;
          var score1 = document.getElementById("score1").value;
          var team2 = document.getElementById("team2").value;
          var score2 = document.getElementById("score2").value;
          if (team1 === team2) {
            alert("Team 1 and Team 2 must be different");
            return false;
          }
          var date = document.getElementById("date").value;
          
          if (team1 === "" || score1 === "" || team2 === "" || score2 === "" || date === "") {
            alert("All fields are required");
            return false;
          }
          // Validate if the date is today or in the past
          var selectedDate = new Date(date);
          var today = new Date();
          today.setHours(0, 0, 0, 0); // Set time to midnight
          
          if (selectedDate > today) {
            alert("Please select a date that is today or in the past");
            return false;
          }
          // Validate if the scores are digits
          var scorePattern = /^\d+$/;
          if (!scorePattern.test(score1) || !scorePattern.test(score2)) {
            alert("Scores must contain only digits");
            return false;
          }

          return true;
        }

  </script>

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
            <h1 class="text-white">New Game</h1>
            <p>Insert a new game with our intuitive site.</p>
          </div>
        </div>
      </div>
    </div>

    <h2>New Game Entry</h2>

<form action="add_game.php" method="post" onsubmit="return validateForm()">
    <div class="form-group">
        <label for="team1">Team 1<sup>*</sup>:</label>
        <select class="form-control" name="team1" id="team1" required>
          <option value="" disabled selected>Select a team</option>
          <option value="5">Dallas Cowboys</option>
          <option value="6">Chicago Bears</option>
          <option value="7">Baltimore Ravens</option>
          <option value="8">Indianapolis Colts</option>
        </select>
    </div>
    <div class="form-group">
        <label for="score1">Score 1<sup>*</sup>:</label>
        <input class="form-control" type="number" name="score1" id="score1" min="0" required>
    </div>
    <div class="form-group">
        <label for="team2">Team 2<sup>*</sup>:</label>
        <select class="form-control" name="team2" id="team2" required>
          <option value="" disabled selected>Select a team</option>
          <option value="5">Dallas Cowboys</option>
          <option value="6">Chicago Bears</option>
          <option value="7">Baltimore Ravens</option>
          <option value="8">Indianapolis Colts</option>
        </select>
    </div>
    <div class="form-group">
        <label for="score2">Score 2<sup>*</sup>:</label>
        <input class="form-control" type="number" name="score2" id="score2" min="0" required>
    </div>
    <div class="form-group">
        <label for="date">Date<sup>*</sup>:</label>
        <input class="form-control" type="date" id="date" name="date" required>
    </div>

    <input type="hidden" name="submit" value="1">
    <button type="submit" class="btn btn-primary">Submit</button>
</form>




<?php
if (isset($_POST['submit'])) {
  $teamId1 = escapeshellarg($_POST['team1']);
  $teamId2 = escapeshellarg($_POST['team2']);
  $score1 = escapeshellarg($_POST['score1']);
  $score2 = escapeshellarg($_POST['score2']);
  $date = escapeshellarg($_POST['date']);

  $command = 'python3 nfl.py add_game' . ' ' . $teamId1 . ' ' . $teamId2 . ' ' . $score1 . ' ' . $score2 . ' ' . $date;
  // Execute the command and capture the output
  $output = shell_exec($command);

  // Display the output as a success message
  if (strpos($output, 'Game added successfully!') !== false) {
    echo '<div class="alert alert-success" role="alert">Game added successfully!</div>';
} else {
    echo '<div class="alert alert-danger" role="alert">Failed to add the game.</div>';
}
}
?>


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


  <!-- Include jQuery -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <!-- Include Bootstrap JS -->
  <script src="js/bootstrap.min.js"></script>
  <!-- Custom script to close date picker after selection -->
  <script>
    // Wait for the document to be ready
    $(document).ready(function() {
      // Add change event listener to the date input field
      $('#date').on('change', function() {
        // Close the date picker by removing the focus from the input field
        $(this).blur();
      });
    });
  </script>
</body>
</body>

</html>
