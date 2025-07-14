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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RBM_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RBM/RBM_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="8bc08e618f8a4c5f0d7e236219fde6dfe56e440230aeb9e5be64cfea1da37c7a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
