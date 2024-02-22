# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaptpx(RPackage):
	"""MAP Estimation of Topic Models

	Maximum a posteriori (MAP) estimation for topic models (i.e., Latent Dirichlet Allocation) in text analysis,
	as described in Taddy (2012) 'On estimation and selection for topic models'.  Previous versions of this code were included as part of the 'textir' package.  If you want to take advantage of openmp parallelization, uncomment the relevant flags in src/MAKEVARS before compiling.
	"""
	
	homepage = "http://taddylab.com"
	cran = "maptpx" 

	version("1.9-7", md5="caffcd503c07fd413a460fb7832c9422")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
