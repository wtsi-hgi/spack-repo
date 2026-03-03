# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErpeq(RPackage):
	"""Probabilistic Hazard Assessment

	Computes the probability density and cumulative distribution functions of fourteen distributions used for the probabilistic hazard assessment. Estimates the model parameters of the distributions using the maximum likelihood and reports the goodness-of-fit statistics. The recurrence interval estimations of earthquakes are computed for each distribution.
	"""
	
	cran = "ERPeq" 

	version("0.1.0", md5="64685c5a3e65b2d449535dce6944a70b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
