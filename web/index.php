<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Symptoms</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <div class="container">
            <form id="form" class="form predectionForm" action="predection.php" method="post" onsubmit="return false;">
                <img src="logo.png" style="max-width: 100%;margin-bottom: 1rem;">
                <h2>Enter Symptoms</h2>
                <div class="form-control">
                    <textarea name="data" id="data" cols="30" rows="10"></textarea>
                </div>
                <button>Get Prediction</button>

                <p class="error">Symptoms is required</p>
                <p class="prediction"></p>
            </form>
        </div>
    </body>

    <script src="js/jq.js"></script>
    <script src="js/submit.js"></script>
</html>