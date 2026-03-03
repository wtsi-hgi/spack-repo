# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterhd(RPackage):
	"""Tools for Clustering High-Dimensional Data

	Tools for clustering high-dimensional data.
  In particular, it contains the methods described in
   <doi:10.1093/bioinformatics/btaa243>,
   <arXiv:2010.00950>.
	"""
	
	homepage = "https://arxiv.org/abs/2010.00950"
	cran = "clusterHD" 

	version("1.0.2", md5="0c9a8402ea308722c1b6412ce9ccd68f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
