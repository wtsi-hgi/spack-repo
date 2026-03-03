# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYaconsensus(RPackage):
	"""Consensus Clustering of Omic Data

	Procedures to perform consensus clustering starting from a dissimilarity matrix or a data matrix. It's allowed to select if the subsampling has to be by samples or features. In case of computational heavy load, the procedures can run in parallel.
	"""
	
	homepage = "https://github.com/stefanoMP/yaConsensus"
	cran = "yaConsensus" 

	version("1.0", md5="e4626131fbc2a6d8b38730c9f4befe1d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-pheatmap@1.0.12:", type=("build", "run"))
	depends_on("r-doparallel@1.0.16:", type=("build", "run"))
