ModelDriver = function (id, first_name, last_name, email, phone, password) {
    var self = this;

    self.id = ko.observable(id);
    self.first_name = ko.observable(first_name);
    self.last_name = ko.observable(last_name);
    self.email = ko.observable(email);
    self.phone = ko.observable(phone);
    self.password = ko.observable(password);
};


ModelOwner = function (id, name) {
    var self = this;

    self.id = ko.observable(id);
    self.name = ko.observable(name);
};


RegisterDelex = function () {
    var self = this;

    self.owners = ko.observableArray();
    self.drivers = ko.observableArray();

    /*----------------------------------------------------------------------
    * build number of owners
    *--------------------------------------------------------------------*/
    self.numberOfOwners = function () {
        var drpValue = $('#drpOwners').val();
        self.owners.removeAll();
        for (var i = 1; i <= drpValue; i++) {
            var owner = new ModelOwner('owner-name-' + i.toString(), '')
            self.owners.push(owner);
        }
    };

    /*----------------------------------------------------------------------
    * build number of drivers
    *--------------------------------------------------------------------*/
    self.numberOfDrivers = function () {
        var drpValue = $('#drpDrivers').val();
        self.drivers.removeAll();
        for (var i = 1; i <= drpValue; i++) {
            var driver = new ModelDriver(i, '', '', '', '', '')
            self.drivers.push(driver);
        }
    };


    /*----------------------------------------------------------------------
    * INIT
    *---------------------------------------------------------------------*/
    self.init = function () {
        var owner = new ModelOwner('owner-name-1', '')
        var driver = new ModelDriver(1, '', '', '', '', '')
        self.owners.push(owner);
        self.drivers.push(driver);
    };
    self.init();
};

var registerDelex = new RegisterDelex();
ko.applyBindings(registerDelex, document.body);
