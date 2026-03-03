# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisto(RPackage):
	"""Unified Interface to Distance, Dissimilarity, Similarity
Matrices

	Provides a high level API to interface over sources storing distance, dissimilarity, similarity matrices with matrix style extraction, replacement and other utilities. Currently, in-memory dist object backend is supported.
	"""
	
	homepage = "https://github.com/talegari/disto"
	cran = "disto" 

	version("0.2.0", md5="74c0057f16927789b675013ffc16856c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-proxy@0.4.19:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-fastmatch@1.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-factoextra@1.0.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-broom@0.4.4:", type=("build", "run"))
	depends_on("r-fastcluster@1.1.25:", type=("build", "run"))
	depends_on("r-pbapply@1.3.4:", type=("build", "run"))
