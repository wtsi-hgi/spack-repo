# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreener(RPackage):
	"""Geospatial Regression Equation for European Nutrient Losses
(GREEN)

	Tools and methods to apply the model Geospatial Regression Equation
    for European Nutrient losses (GREEN); 
    Grizzetti et al. (2005) <doi:10.1016/j.jhydrol.2004.07.036>; 
    Grizzetti et al. (2008);
    Grizzetti et al. (2012) <doi:10.1111/j.1365-2486.2011.02576.x>; 
    Grizzetti et al. (2021) <doi:10.1016/j.gloenvcha.2021.102281>. 
	"""
	
	homepage = "https://github.com/calfarog/GREENeR"
	cran = "GREENeR" 

	version("1.0.0", md5="a81a971fa80d82dbaa4903e51b112e4b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fme@1.3.6.1:", type=("build", "run"))
	depends_on("r-data-table@1.13.6:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-sf@1.0.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-tmap@3.3.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-classint@0.4.3:", type=("build", "run"))
	depends_on("r-networkd3@0.4:", type=("build", "run"))
	depends_on("r-parallelly@1.30:", type=("build", "run"))
