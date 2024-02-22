# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImagedata(RPackage):
	"""Aids in Processing and Plotting Data from a Lemna-Tec
Scananalyzer

	Note that 'imageData' has been superseded by 'growthPheno'. 
    The package 'growthPheno' incorporates all the functionality of 
    'imageData' and has functionality not available in 'imageData', 
    but some 'imageData' functions have been renamed.  
    The 'imageData' package is no longer maintained, but is retained 
    for legacy purposes. 
	"""
	
	homepage = "http://chris.brien.name"
	cran = "imageData" 

	version("0.1-62", md5="fff2bc102311714476ca99a00bf3ec04")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dae", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
