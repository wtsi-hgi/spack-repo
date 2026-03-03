# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSop(RPackage):
	"""Generalised Additive P-Spline Regression Models Estimation

	Generalised additive P-spline regression models estimation using the separation of overlapping precision matrices (SOP) method. Estimation is based on the equivalence between P-splines and linear mixed models, and variance/smoothing parameters are estimated based on restricted maximum likelihood (REML). The package enables users to estimate P-spline models with overlapping penalties. Based on the work described in Rodriguez-Alvarez et al. (2015) <doi:10.1007/s11222-014-9464-2>; Rodriguez-Alvarez et al. (2019) <doi:10.1007/s11222-018-9818-2>, and Eilers and Marx (1996) <doi:10.1214/ss/1038425655>.
	"""
	
	cran = "SOP" 

	version("1.0-1", md5="ab6d12384e7f35b0406d4819817d28a1")

	depends_on("r-mass", type=("build", "run"))
