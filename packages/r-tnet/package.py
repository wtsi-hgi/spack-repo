# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTnet(RPackage):
	"""Weighted, Two-Mode, and Longitudinal Networks Analysis

	Binary ties limit the richness of network analyses as relations are unique. The two-mode structure contains a number of features lost when projection it to a one-mode network. Longitudinal datasets allow for an understanding of the causal relationship among ties, which is not the case in cross-sectional datasets as ties are dependent upon each other.
	"""
	
	homepage = "http://toreopsahl.com/tnet/"
	cran = "tnet" 

	version("3.0.16", md5="3d6bf7a901c21e534e01d524f386a473")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
