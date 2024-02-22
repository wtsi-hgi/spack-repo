# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartp(RPackage):
	"""Sample Size for SMART Designs in Non-Surgical Periodontal Trials

	Sample size calculation to detect dynamic treatment regime (DTR) effects based on change in clinical attachment level (CAL) outcomes from a non-surgical chronic periodontitis treatments study. The experiment is performed under a Sequential Multiple Assignment Randomized Trial (SMART) design. The clustered tooth (sub-unit) level CAL outcomes are skewed, spatially-referenced, and non-randomly missing. The implemented algorithm is available in Xu et al. (2019+) <arXiv:1902.09386>.
	"""
	
	homepage = "https://github.com/bandyopd/SMARTp"
	cran = "SMARTp" 

	version("0.1.1", md5="7ab4ec4979c18f1c8f3ab3b3ba8a2075")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-covr", type=("build", "run"))
	depends_on("r-sn@1.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1:", type=("build", "run"))
