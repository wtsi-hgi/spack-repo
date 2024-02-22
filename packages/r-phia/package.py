# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhia(RPackage):
	"""Post-Hoc Interaction Analysis

	Analysis of terms in linear, generalized and mixed linear models, 
	on the basis of multiple comparisons of factor contrasts.  Specially suited 
	for the analysis of interaction terms.
	"""
	
	homepage = "https://github.com/heliosdrm/phia"
	cran = "phia" 

	version("0.3-1", md5="ff5b97a39dba04802d0c9906ebf54896")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
