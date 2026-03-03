# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelayedeffectDesign(RPackage):
	"""Sample Size and Power Calculations using the APPLE, SEPPLE,
APPLE+ and SEPPLE+ Methods

	Provides sample size and power calculations when the treatment time-lag effect is present and the lag duration is either homogeneous across the individual subject, or varies heterogeneously from individual to individual within a certain domain and following a specific pattern. The methods used are described in Xu, Z., Zhen, B., Park, Y., & Zhu, B. (2017) <doi:10.1002/sim.7157>.
	"""
	
	cran = "DelayedEffect.Design" 

	version("1.1.3", md5="d4845a9f828eb51160565e1fb701a7e0")

	depends_on("r@3.5:", type=("build", "run"))
