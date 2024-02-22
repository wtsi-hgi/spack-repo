# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtg(RPackage):
	"""Methods to Analyse Seasonal Radial Tree Growth Data

	Methods for comparing different regression algorithms for 
    describing the temporal dynamics of secondary tree growth (xylem and 
    phloem). Users can compare the accuracy of the most common fitting methods 
    usually used to analyse xylem and phloem data, i.e., Gompertz function, 
    Double Gompertz function, General Additive Models (GAMs); and an algorithm 
    newly introduced to the field, i.e., Bayesian Regularised Neural Networks 
    (brnn). The core function of the package is XPSgrowth(), while the results 
    can be interpreted using implemented generic S3 methods, such as plot() and 
    summary().
	"""
	
	homepage = "https://github.com/jernejjevsenak/rTG"
	cran = "rTG" 

	version("1.0.2", md5="8d717ae60fcde626deb903e5c287e2c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-brnn@0.6:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-mgcv@1.8.34:", type=("build", "run"))
	depends_on("r-knitr@1.19:", type=("build", "run"))
	depends_on("r-dplyr@0.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
