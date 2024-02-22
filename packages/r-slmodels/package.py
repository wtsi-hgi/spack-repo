# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlmodels(RPackage):
	"""Stepwise Linear Models for Binary Classification Problems under
Youden Index Optimisation

	Stepwise models for the optimal linear combination of continuous variables in binary classification problems under Youden Index optimisation. Information on the models implemented can be found at Aznar-Gimeno et al. (2021) <doi:10.3390/math9192497>.
	"""
	
	cran = "SLModels" 

	version("0.1.2", md5="91dcf88c54e1959ff858c564581de401")

	depends_on("r-rocr", type=("build", "run"))
