# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetmcd(RPackage):
	"""Implementation of the DetMCD Algorithm (Robust and Deterministic
Estimation of Location and Scatter)

	Implementation of DetMCD, a new algorithm for robust and deterministic estimation of location and scatter. The benefits of robust and deterministic estimation are explained in Hubert, Rousseeuw and Verdonck (2012) <doi:10.1080/10618600.2012.672100>.
	"""
	
	cran = "DetMCD" 

	version("0.0.5", md5="1503cd55bdebb9f6c0004fef78b58b64")

	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
