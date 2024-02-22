# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWarbler(RPackage):
	"""Streamline Bioacoustic Analysis

	Functions aiming to facilitate the analysis of the structure of animal acoustic signals in 'R'. 'warbleR' makes use of the basic sound analysis tools from the package 'seewave', and offers new tools for acoustic structure analysis. The main features of the package are the use of loops to apply tasks through acoustic signals referenced in a selection (annotation) table and the production of spectrograms in image files that allow to organize data and verify acoustic analyzes. The package offers functions to explore, organize and manipulate multiple sound files, explore and download 'Xeno-Canto' recordings, detect signals automatically, create spectrograms of complete recordings or individual signals, run different measures of acoustic signal structure, evaluate the performance of measurement methods, catalog signals, characterize different structural levels in acoustic signals, run statistical analysis of duet coordination and consolidate databases and annotation tables, among others.
	"""
	
	homepage = "https://marce10.github.io/warbleR/"
	cran = "warbleR" 

	version("1.1.30", md5="29c0519e8c2c30968c8b76cd144f1e70")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-seewave@2.0.1:", type=("build", "run"))
	depends_on("r-naturesounds", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
	depends_on("r-monitor", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-bioacoustics", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
	depends_on("sox", type=("build", "link", "run"))
	depends_on("ghostscript", type=("build", "link", "run"))
	depends_on("libsndfile", type=("build", "link", "run"))
	depends_on("gdal", type=("build", "link", "run"))
