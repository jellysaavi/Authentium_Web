
//we can set animation delay as following in ms (default 1000)
ProgressBar.singleStepAnimation = 4500;
ProgressBar.init(
  [ 'In transit ',
    'OUt for delivery  ',
   
    'delivered '
   
  ],
  'delivered ',
  'progress-bar-wrapper' // created this optional parameter for container name (otherwise default container created)
);