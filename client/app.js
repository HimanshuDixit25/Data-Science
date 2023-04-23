from server import predict_average(data:input)

function onClickedEstimatePrice() {
    
    document.getElementById('r1')
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var url = "http://127.0.0.1:8000/predict";

