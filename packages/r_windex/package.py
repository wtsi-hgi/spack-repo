# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWindex(RPackage):
	"""Analysing Convergent Evolution using the Wheatsheaf Index

	Analysing convergent evolution using the Wheatsheaf index, described in Arbuckle et al. (2014) <doi: 10.1111/2041-210X.12195>, and some other unrelated but perhaps useful functions.
	"""
	
	cran = "windex" 

	version("2.0.7", md5="d12d878064abe647a6036c070f1d453d")

	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-geiger@2:", type=("build", "run"))
	depends_on("r-ape@4:", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
