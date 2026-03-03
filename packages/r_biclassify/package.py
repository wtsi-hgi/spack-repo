# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiclassify(RPackage):
	"""Binary Classification Using Extensions of Discriminant Analysis

	Implements methods for sample size 
  reduction within Linear and Quadratic Discriminant Analysis in Lapanowski and Gaynanova (2020) <arXiv:2005.03858>.
  Also includes methods for non-linear discriminant analysis with simultaneous sparse feature selection in Lapanowski and Gaynanova (2019) PMLR 89:1704-1713. 
	"""
	
	cran = "biClassify" 

	version("1.3", md5="c2c522cff1cb2db8d7fc27290e72a754")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-daag", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
