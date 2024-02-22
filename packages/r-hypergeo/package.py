# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypergeo(RPackage):
	"""The Gauss Hypergeometric Function

	The Gaussian hypergeometric function for complex numbers.
	"""
	
	cran = "hypergeo" 

	version("1.2-13", md5="fe7a150c10ab854fa5f6d70ee0f7549e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-elliptic@1.3.5:", type=("build", "run"))
	depends_on("r-contfrac@1.1.9:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
