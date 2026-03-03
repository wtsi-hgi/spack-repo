# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLincal(RPackage):
	"""Static Univariate Frequentist and Bayesian Linear Calibration

	Estimate and confidence/credible intervals for an unknown
    regressor x0 given an observed y0.
	"""
	
	cran = "LinCal" 

	version("1.0.1", md5="7fe4d6847a1b593caad52098de04ecaa")

	depends_on("r@3.0.2:", type=("build", "run"))
