# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCertainty(RPackage):
	"""Certainty Equivalent

	Compute the certainty equivalents and premium risks
              as tools for risk-efficiency analysis. For more technical information, please refer to: Hardaker, Richardson, Lien, & Schumann (2004) <doi:10.1111/j.1467-8489.2004.00239.x>, and Richardson, & Outlaw (2008) <doi:10.2495/RISK080231>.
	"""
	
	cran = "ceRtainty" 

	version("1.0.0", md5="b2a488735f81930b43a6844075fcc56d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
