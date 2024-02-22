# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmoc(RPackage):
	"""Multi-Omic Spectral Clustering using the Flag Manifold

	Multi-omic (or any multi-view) spectral clustering methods often assume the same number of clusters across all datasets. We supply methods for multi-omic spectral clustering when the number of distinct clusters differs among the omics profiles (views). 
	"""
	
	cran = "MMOC" 

	version("0.1.1.0", md5="6d8fd61f20efa2ced3d60315d7858977")

	depends_on("r-spectrum@1.1:", type=("build", "run"))
	depends_on("r-igraph@1.4.1:", type=("build", "run"))
	depends_on("r-mass@7.3.58.1:", type=("build", "run"))
