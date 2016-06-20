var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('default', ['sass:watch']);

gulp.task('sass', function () {
  return gulp.src('./media/sass/styles.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./media/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./public/sass/**/*.scss', ['sass', 'inject']);
});

// \Big[\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V\Big]\Psi = i\hbar \frac{\partial}{\partial t} \Psi

gulp.task('inject', function(){
    var wiredep = require('wiredep').stream;
    var inject = require('gulp-inject');

    var injectSrc = gulp.src([
      './media/folio/js/**/*.js',
      './media/js/**/*.js',
      './media/folio/css/**/*.css',
      './media/css/**/*.css',
    ], {read: false});

    var injectOptions = {
        ignorePath: '/media/',
        addPrefix: '/static'
    };

    var options = {
        bowerJson: require('./bower.json'),
        directory: './media/lib',
        ignorePath: '../media',
        fileTypes: {
          html: {
            replace: {
              js: '<script src="/static{{filePath}}"></script>',
              css: '<link rel="stylesheet" href="/static{{filePath}}" />'
            }
          }
        }
    };

    gulp.src('./templates/index.html')
        .pipe(wiredep(options))
        .pipe(inject(injectSrc, injectOptions))
        .pipe(gulp.dest('./templates'));

    injectSrc = gulp.src([
      './media/js/**/*.js',
      './media/css/**/*.css',
    ], {read: false});

    gulp.src('./templates/account.html')
        .pipe(wiredep(options))
        .pipe(inject(injectSrc, injectOptions))
        .pipe(gulp.dest('./templates'));

});
