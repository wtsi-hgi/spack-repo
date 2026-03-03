# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmmreml(RPackage):
	"""Fitting Mixed Models with Known Covariance Structures

	The main functions are 'emmreml', and 'emmremlMultiKernel'. 'emmreml' solves a mixed model with known covariance structure using the 'EMMA' algorithm.  'emmremlMultiKernel' is a wrapper for 'emmreml' to handle multiple random components with known covariance structures. The function 'emmremlMultivariate' solves a multivariate gaussian mixed model with known covariance structure using the 'ECM' algorithm.
	"""
	
	cran = "EMMREML" 

	version("3.1", md5="d5e185865810ad9c0eba3b8b06e3ef2f")

	depends_on("r-matrix", type=("build", "run"))
