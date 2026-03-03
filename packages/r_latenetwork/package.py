# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatenetwork(RPackage):
	"""Inference on LATEs under Network Interference of Unknown Form

	Estimating causal parameters in the presence of treatment spillover is of great interest in statistics.
    This package provides tools for instrumental variables estimation of average causal effects under network interference of unknown form.
    The target parameters are the local average direct effect, the local average indirect effect, the local average overall effect, and the local average spillover effect.
    The methods are developed by Hoshino and Yanagi (2023) <doi:10.48550/arXiv.2108.07455>.
	"""
	
	homepage = "https://tkhdyanagi.github.io/latenetwork/"
	cran = "latenetwork" 

	version("1.0.1", md5="08dc17db70b85e874e3927416c8456c0")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-statip", type=("build", "run"))
