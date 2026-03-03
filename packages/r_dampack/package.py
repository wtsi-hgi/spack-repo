# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDampack(RPackage):
	"""Decision-Analytic Modeling Package

	A suite of functions for analyzing and visualizing the health economic outputs of mathematical models.
    This package was developed with funding from the National Institutes of Allergy and Infectious Diseases of the 
    National Institutes of Health under award no. R01AI138783. The content of this package is solely the 
    responsibility of the authors and does not necessarily represent the official views of the National Institutes 
    of Health. The theoretical underpinnings of 'dampack''s functionality are detailed in Hunink et al. (2014) 
    <doi:10.1017/CBO9781139506779>.
	"""
	
	homepage = "https://github.com/DARTH-git/dampack"
	cran = "dampack" 

	version("1.0.1", md5="9cbf45af2c6a2662ded6387ffbab613e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
