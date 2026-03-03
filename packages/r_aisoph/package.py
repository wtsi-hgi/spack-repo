# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAisoph(RPackage):
	"""Additive Isotonic Proportional Hazards Model

	Nonparametric estimation of additive isotonic covariate effects for proportional hazards model.
	"""
	
	cran = "aisoph" 

	version("0.4", md5="05003bd32e7ceee0927b2064c8f221b7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
