var gulp = require('gulp'),
    sass = require('gulp-sass'),
    neat = require('node-neat').includePaths,
    minifycss = require('gulp-minify-css'),
    rename = require('gulp-rename'),
    watch = require('gulp-watch');

gulp.task('sass', function() {
    return gulp.src('static/scss/*.scss')
        .pipe(sass({
          includePaths: ['styles'].concat(neat)
        }))
        .pipe(gulp.dest('static/css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('static/css'));
});

gulp.task('watch', function() {
    gulp.watch('static/scss/*.scss', ['sass']);
});

gulp.task('default', ['sass', 'watch']);
