# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustlm(RPackage):
	"""Robust Variable Selection with Exponential Squared Loss

	Computationally efficient tool for performing variable selection and obtaining robust estimates, which implements robust variable selection procedure proposed by Wang, X., Jiang, Y., Wang, S., Zhang, H. (2013) <doi:10.1080/01621459.2013.766613>. Users can enjoy the near optimal, consistent, and oracle properties of the procedures. 
	"""
	
	cran = "robustlm" 

	version("0.1.0", md5="32ebb829bd557bbfaa0596a778287cda")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
