# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobusthd(RPackage):
	"""Robust Methods for High-Dimensional Data

	Robust methods for high-dimensional data, in particular linear
    model selection techniques based on least angle regression and sparse
    regression. Specifically, the package implements robust least angle 
    regression (Khan, Van Aelst & Zamar, 2007; <doi:10.1198/016214507000000950>), 
    (robust) groupwise least angle regression (Alfons, Croux & Gelper, 2016; 
    <doi:10.1016/j.csda.2015.02.007>), and sparse least trimmed squares 
    regression (Alfons, Croux & Gelper, 2013; <doi:10.1214/12-AOAS575>).
	"""
	
	homepage = "https://github.com/aalfons/robustHD"
	cran = "robustHD" 

	version("0.8.0", md5="9871008e3fe9af8b8d38788624fc2ec1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
	depends_on("r-perry@0.3:", type=("build", "run"))
	depends_on("r-robustbase@0.9.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp@0.9.10:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.3:", type=("build", "run"))
