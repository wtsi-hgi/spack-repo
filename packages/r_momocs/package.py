# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMomocs(RPackage):
	"""Morphometrics using R

	The goal of 'Momocs' is to provide a complete, convenient, 
       reproducible and open-source toolkit for 2D morphometrics.
       It includes most common 2D morphometrics approaches on outlines, open outlines, 
       configurations of landmarks, traditional morphometrics, and facilities for data preparation, 
       manipulation and visualization with a consistent grammar throughout.
       It allows reproducible, complex morphometrics analyses and other morphometrics approaches 
       should be easy to plug in, or develop from, on top of this canvas. 
	"""
	
	homepage = "https://github.com/MomX/Momocs/"
	cran = "Momocs" 

	version("1.4.1", md5="15d4140dada16ed11ad62226f8833b00")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-geomorph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
