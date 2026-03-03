# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyncorr(RPackage):
	"""Dynamic Correlation Package

	Computes dynamical correlation estimates and percentile
        bootstrap confidence intervals for pairs of longitudinal
        responses, including consideration of lags and derivatives.
	"""
	
	cran = "dynCorr" 

	version("1.1.0", md5="d02c71fdfd0197210a04fd9d61457f49")

	depends_on("r-lpridge", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
