# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSatdad(RPackage):
	"""Sensitivity Analysis Tools for Dependence and Asymptotic
Dependence

	Tools for analyzing tail dependence in any sample or in particular theoretical models.  The package uses only theoretical and non parametric methods, without inference.  The primary goals of the package are to provide: (a)symmetric multivariate extreme value models in any dimension;  theoretical and empirical indices to order tail dependence;  theoretical and empirical graphical methods to visualize tail dependence. 
	"""
	
	cran = "satdad" 

	version("1.1", md5="8952560785f4c85a1cf62895271c812b")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-graphicalextremes", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
