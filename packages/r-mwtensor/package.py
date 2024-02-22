# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwtensor(RPackage):
	"""Multi-Way Component Analysis

	For single tensor data, any matrix factorization method can be specified the matricised tensor in each dimension by Multi-way Component Analysis (MWCA). An originally extended MWCA is also implemented to specify and decompose multiple matrices and tensors simultaneously (CoupledMWCA). See the reference section of GitHub README.md <https://github.com/rikenbit/mwTensor>, for details of the methods.
	"""
	
	homepage = "https://github.com/rikenbit/mwTensor"
	cran = "mwTensor" 

	version("1.1.0", md5="0abb81eef326574b2c3098d914c9f81e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-nntensor", type=("build", "run"))
	depends_on("r-cctensor", type=("build", "run"))
	depends_on("r-itensor", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
