# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNntensor(RPackage):
	"""Non-Negative Tensor Decomposition

	Some functions for performing non-negative matrix factorization, non-negative CANDECOMP/PARAFAC (CP) decomposition, non-negative Tucker decomposition, and generating toy model data. See Andrzej Cichock et al (2009) and the reference section of GitHub README.md <https://github.com/rikenbit/nnTensor>, for details of the methods.
	"""
	
	homepage = "https://github.com/rikenbit/nnTensor"
	cran = "nnTensor" 

	version("1.2.0", md5="d1a1219ab3fdceede482a6719dd5f770")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-tagcloud", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
