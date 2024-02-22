# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdbetareg(RPackage):
	"""Ordered Beta Regression Models with 'brms'

	Implements ordered beta regression models, which are for modeling continuous variables with upper and lower bounds, such as
   survey sliders, dose-response relationships and indexes. For more information, see
   Kubinec (2022) <doi:10.31235/osf.io/2sx6y>. The package is a front-end to the R package 'brms', which 
   facilitates a range of regression specifications, including hierarchical, dynamic and
   multivariate modeling.
	"""
	
	cran = "ordbetareg" 

	version("0.7.2", md5="19052e5ddff3b0f7a4166f293bde3a1a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-brms@2.18:", type=("build", "run"))
	depends_on("r-transformr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
