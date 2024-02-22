# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimfit(RPackage):
	"""Test Model Fit with Simulation

	Simulates data from model objects (e.g., from lm(), glm()),
    and plots this along with the original data to compare how well the
    simulated data matches the original data to determine model fit.
	"""
	
	cran = "simfit" 

	version("0.1.0", md5="69414f190f4128cc9aef9d4394f3e92a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
