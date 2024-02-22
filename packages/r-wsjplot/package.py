# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWsjplot(RPackage):
	"""Style Time Series Plots Like the Wall Street Journal

	Easily override the default visual choices in 'ggplot2' to make 
    your time series plots look more like the Wall Street Journal. Specific 
    theme design choices include omitting x-axis grid lines and displaying 
    sparse light grey y-axis grid lines. Additionally, this allows to label 
    the y-axis scales with your units only displayed on the top-most number, 
    while also removing the bottom most number (unless specifically 
    overridden). The goal is visual simplicity, because who has time to waste 
    looking at a cluttered graph? 
	"""
	
	cran = "wsjplot" 

	version("0.1.0", md5="edb2c838d59ce266b6e1af6411afc9fc")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
