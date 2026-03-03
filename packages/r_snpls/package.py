# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpls(RPackage):
	"""NPLS Regression with L1 Penalization

	Tools for performing variable selection in three-way data using N-PLS 
    in combination with L1 penalization, Selectivity Ratio and VIP scores. 
    The N-PLS model (Rasmus Bro, 1996 <DOI:10.1002/(SICI)1099-128X(199601)10:1%3C47::AID-CEM400%3E3.0.CO;2-C>) 
    is the natural extension of PLS (Partial Least Squares) to N-way structures, and tries 
    to maximize the covariance between X and Y data arrays. The package also adds
    variable selection through L1 penalization, Selectivity Ratio and VIP scores.
	"""
	
	cran = "sNPLS" 

	version("1.0.27", md5="d863ebaa3d646e3870614cb20fe530e2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-clickr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
