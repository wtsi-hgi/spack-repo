# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobreg3s(RPackage):
	"""Three-Step Regression and Inference for Cellwise and Casewise
Contamination

	Three-step regression and inference for cellwise and casewise contamination.
	"""
	
	cran = "robreg3S" 

	version("0.3", md5="0881d0668bf94a915629b5519a151fee")

	depends_on("r-gse", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
