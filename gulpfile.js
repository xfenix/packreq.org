const rootDir = './packreq/'
const fromDir = rootDir + 'prestatic/'
const stylesDir = fromDir + 'css/'
const toDir = rootDir + 'static/'
const gulp = require('gulp')
const postcss = require('gulp-postcss')
const concatImport = require('gulp-concat-css-import')
const autoprefixer = require('autoprefixer')
const cssnext = require('cssnext')
const precss = require('precss')


gulp.task('css', function() {
    var processors = [
        autoprefixer({browsers: ['last 1 version']}),
        cssnext,
        precss
    ]
    return gulp.src(stylesDir + 'index.css')
        .pipe(postcss(processors))
        .pipe(concatImport({rootPath: stylesDir, isCompress: true}))
        .pipe(gulp.dest(toDir))
})
