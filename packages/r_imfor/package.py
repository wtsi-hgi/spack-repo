# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImfor(RPackage):
	"""Non-Linear Height Diameter Models for Forestry

	Tree height is an important dendrometric variable and forms the basis of vertical structure of a forest stand. This package will help to fit and validate various non-linear height diameter models for assessing the underlying relationship that exists between tree height and diameter at breast height in case of conifer trees. This package has been implemented on Naslund, Curtis, Michailoff, Meyer, Power, Michaelis-Menten and Wykoff non linear models using algorithm of  Huang et al.  (1992) <doi:10.1139/x92-172> and Zeide et al. (1993) <doi:10.1093/forestscience/39.3.594>.
	"""
	
	cran = "ImFoR" 

	version("0.1.0", md5="759338f88385772d32b3a5b2bd8e61c6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
