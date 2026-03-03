# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGawdis(RPackage):
	"""Multi-Trait Dissimilarity with more Uniform Contributions

	R function gawdis() produces multi-trait dissimilarity with more uniform contributions of different traits. de Bello et al. (2021) <doi:10.1111/2041-210X.13537> presented the approach based on minimizing the differences in the correlation between the dissimilarity of each trait, or groups of traits, and the multi-trait dissimilarity. This is done using either an analytic or a numerical solution, both available in the function.
	"""
	
	homepage = "https://github.com/pavel-fibich/gawdis/"
	cran = "gawdis" 

	version("0.1.5", md5="e7c0e14f6f091bdb209a9321881c50f4")

	depends_on("r-fd", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
