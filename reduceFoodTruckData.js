var fileParse = function(file) {
    var parsedFile = require(file);
    return parsedFile.restaurants.filter(function(restaurant) {
        return restaurant.restaurant.city_name === "Los Angeles";
    }).map(function(restaurant) {
        return {"name":restaurant.restaurant.name, "twitter_screenname":restaurant.restaurant.twitter_screenname};
    });
}

var fileWrite = function(object) {
    var fs = require('fs');
    fs.writeFile('./parseOut.json', JSON.stringify(object, null, 2), function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
    }); 
}

fileWrite(fileParse('./foodTrucks.json'));

