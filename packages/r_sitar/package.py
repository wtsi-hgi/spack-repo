# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitar(RPackage):
	"""Super Imposition by Translation and Rotation Growth Curve
Analysis

	Functions for fitting and plotting SITAR (Super
    Imposition by Translation And Rotation) growth curve models. SITAR is
    a shape-invariant model with a regression B-spline mean curve and
    subject-specific random effects on both the measurement and age
    scales.  The model was first described by Lindstrom (1995)
    <doi:10.1002/sim.4780141807> and developed as the SITAR method by Cole
    et al (2010) <doi:10.1093/ije/dyq115>.
	"""
	
	homepage = "https://github.com/statist7/sitar"
	cran = "sitar" 

	version("1.4.0", md5="1fb44ccab9e0116654f12f320b65a392")
	version("1.3.0", md5="ebe27b357b4fe59bc4f87ecb74a0e2e9")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
