# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSantar(RPackage):
	"""Short Asynchronous Time-Series Analysis

	A graphical and automated pipeline for the analysis 
		of short time-series in R ('santaR'). This approach is designed to accommodate asynchronous 
		time sampling (i.e. different time points for different individuals), 
		inter-individual variability, noisy measurements and large numbers of variables. 
		Based on a smoothing splines functional model, 'santaR' is able to detect variables
		highlighting significantly different temporal trajectories between study groups.
		Designed initially for metabolic phenotyping, 'santaR' is also suited for other Systems Biology 
		disciplines. Command line and graphical analysis (via a 'shiny' application) enable fast and
		parallel automated analysis and reporting, intuitive visualisation and comprehensive plotting
		options for non-specialist users.
	"""
	
	homepage = "https://github.com/adwolfer/santaR"
	cran = "santaR" 

	version("1.2.4", md5="315b7cdbf23261882aa8a993e8de6be1")
	version("1.2.3", md5="de37ac6c1e50b1003084245a8a269928")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.9:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-pcamethods@1.92:", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-iterators@1.0.9:", type=("build", "run"))
	depends_on("r-shiny@1.8:", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-dt@0.9:", type=("build", "run"))
