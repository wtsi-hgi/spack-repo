# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseede(RPackage):
	"""iSEE extension for panels related to differential expression analysis

	This package contains diverse functionality to extend the usage of the iSEE package, including additional classes for the panels or modes facilitating the analysis of differential expression results. This package does not perform differential expression. Instead, it provides methods to embed precomputed differential expression results in a SummarizedExperiment object, in a manner that is compatible with interactive visualisation in iSEE applications.
	"""
	
	homepage = "https://github.com/iSEE/iSEEde"
	bioc = "iSEEde"

	version("1.6.0", commit="da8514d103d95f0afa4a0ca705a3a10848eee3e9")
	version("1.0.0", commit="bfb3b22aa6dd57a4c2830ba1b5eef1f3dcdee188")

	depends_on("r-isee", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
