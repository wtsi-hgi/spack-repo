# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgcompint(RPackage):
	"""Quantile G-Computation Extensions for Effect Measure
Modification

	G-computation for a set of time-fixed exposures
    with quantile-based basis functions, possibly under linearity and
    homogeneity assumptions. Effect measure modification in this method is a way
    to assess how the effect of the mixture varies by a binary, categorical or continuous variable.  
    Reference: Alexander P. Keil, Jessie P.
    Buckley, Katie M. OBrien, Kelly K. Ferguson, Shanshan Zhao, and
    Alexandra J. White (2019) A quantile-based g-computation approach to
    addressing the effects of exposure mixtures; <doi:10.1289/EHP5838>.
	"""
	
	homepage = "https://github.com/alexpkeil1/qgcomp/"
	cran = "qgcompint" 

	version("0.7.0", md5="9d8d9ef9c120de4c7c0d26cad0832aa0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-qgcomp", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
