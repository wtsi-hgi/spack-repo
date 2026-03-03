# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPupilpre(RPackage):
	"""Preprocessing Pupil Size Data

	Pupillometric data collected using SR Research Eyelink eye trackers 
    requires significant preprocessing. This package contains functions for 
    preparing pupil dilation data for visualization and statistical analysis. 
    Specifically, it provides a pipeline of functions which aid in data validation,
    the removal of blinks/artifacts, downsampling, and baselining, among others. 
    Additionally, plotting functions for creating grand average and conditional 
    average plots are provided. See the vignette for samples of the functionality.
    The package is designed for handling data collected with SR Research 
    Eyelink eye trackers using Sample Reports created in SR Research Data 
    Viewer. 
	"""
	
	cran = "PupilPre" 

	version("0.6.2", md5="82f409454be5a7f4037ab2fd527ccf75")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-rlang@0.1.1:", type=("build", "run"))
	depends_on("r-vwpre@1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-mgcv@1.8.16:", type=("build", "run"))
	depends_on("r-shiny@0.14.2:", type=("build", "run"))
	depends_on("r-tidyr@0.6:", type=("build", "run"))
	depends_on("r-robustbase@0.93.3:", type=("build", "run"))
	depends_on("r-zoo@1.8.4:", type=("build", "run"))
	depends_on("r-signal@0.7.6:", type=("build", "run"))
