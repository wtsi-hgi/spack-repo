# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdfs(RPackage):
	"""MultiDimensional Feature Selection

	Functions for MultiDimensional Feature Selection (MDFS):
 calculating multidimensional information gains, scoring variables,
 finding important variables, plotting selection results.
 This package includes an optional CUDA implementation that speeds up
 information gain calculation using NVIDIA GPGPUs.
 R. Piliszek et al. (2019) <doi:10.32614/RJ-2019-019>.
	"""
	
	homepage = "https://www.mdfs.it/"
	cran = "MDFS" 

	version("1.5.3", md5="219152e8827a9b7a6f1e1e1a3cce2754")

	depends_on("r@3.4:", type=("build", "run"))
