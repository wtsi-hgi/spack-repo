# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbm(RPackage):
	"""RBM: a R package for microarray and RNA-Seq data analysis

	Use A Resampling-Based Empirical Bayes Approach to Assess Differential Expression in Two-Color Microarrays and RNA-Seq data sets.
	"""
	
	bioc = "RBM"

	version("1.40.0", commit="3afa95c1d0c4f07d23fbe9c515a4eea6daa28250")
	version("1.34.0", commit="3913399b2c91d9f5d2dd98875ab59ad0b624ad69")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
