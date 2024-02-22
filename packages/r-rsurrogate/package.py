# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsurrogate(RPackage):
	"""Robust Estimation of the Proportion of Treatment Effect
Explained by Surrogate Marker Information

	Provides functions to estimate the proportion of treatment effect on the primary outcome that is explained by the treatment effect on the surrogate marker. 
	"""
	
	cran = "Rsurrogate" 

	version("3.2", md5="899b757e93c61ee7dd918ee7bfda57bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
