# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialtime(RPackage):
	"""Spatial Analysis of Vectra Immunoflourescent Data

	Visualization and analysis  of Vectra Immunoflourescent
    data. Options for calculating both the univariate and bivariate Ripley's K
    are included. Calculations are performed using a permutation-based 
    approach presented by Wilson et al.  <doi:10.1101/2021.04.27.21256104>. 
	"""
	
	homepage = "https://github.com/FridleyLab/spatialTIME"
	cran = "spatialTIME" 

	version("1.3.4-3", md5="baf195da46998231651f7066f1749af3")
	version("1.3.4-2", md5="9e6dfe6d0071140b1c102b9aad6caa5c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-dixon", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
