# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsmeans(RPackage):
	"""Least-Squares Means

	Obtain least-squares means for linear, generalized linear, 
    and mixed models. Compute contrasts or linear functions of 
    least-squares means, and comparisons of slopes. 
    Plots and compact letter displays. Least-squares means were proposed in
    Harvey, W (1960) "Least-squares analysis of data with unequal subclass numbers",
    Tech Report ARS-20-8, USDA National Agricultural Library, and discussed
    further in Searle, Speed, and Milliken (1980) "Population marginal means 
    in the linear model: An alternative to least squares means", 
    The American Statistician 34(4), 216-221 <doi:10.1080/00031305.1980.10483031>.
    NOTE: lsmeans now relies primarily on code in the 'emmeans' package.
    'lsmeans' will be archived in the near future.
	"""
	
	cran = "lsmeans" 

	version("2.30-0", md5="4295c1ca10213e7c85551d39982afb80")

	depends_on("r-emmeans@1.3:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
