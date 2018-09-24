const rootDir = './packreq/'
const fromDir = rootDir + 'prestatic/'
const toDir = rootDir + 'static/'
const gulp = require('gulp')
const postcss = require('gulp-postcss')


gulp.task('css', function() {
    var processors = [
        autoprefixer({browsers: ['last 1 version']}),
        cssnext,
        precss
    ]
    return gulp.src(fromDir + 'css/*.css')
        .pipe(postcss(processors))
        .pipe(gulp.dest(toDir))
})
