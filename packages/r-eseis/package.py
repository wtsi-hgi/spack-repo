# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REseis(RPackage):
	"""Environmental Seismology Toolbox

	Environmental seismology is a scientific field that studies the  
    seismic signals, emitted by Earth surface processes. This package 
    provides all relevant functions to read/write seismic data files, prepare, 
    analyse and visualise seismic data, and generate reports of the processing 
    history.
	"""
	
	cran = "eseis" 

	version("0.7.3", md5="6b48f3424fe32378a881177ec627b0af")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-irisseismic", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-rcpp@0.12.5:", type=("build", "run"))
