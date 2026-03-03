# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnifed(RPackage):
	"""The Unifed Distribution

	Probability functions, family for glm() and Stan code for working with the unifed distribution (Quijano Xacur, 2019; <doi:10.1186/s40488-019-0102-6>).
	"""
	
	cran = "unifed" 

	version("1.1.6", md5="6d15e906711497d5bfefe3818ff4fe7f")

	depends_on("r@3.1:", type=("build", "run"))
