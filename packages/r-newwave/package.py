# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewwave(RPackage):
	"""Negative binomial model for scRNA-seq

	A model designed for dimensionality reduction and batch effect removal for scRNA-seq data. It is designed to be massively parallelizable using shared objects that prevent memory duplication, and it can be used with different mini-batch approaches in order to reduce time consumption. It assumes a negative binomial distribution for the data with a dispersion parameter that can be both commonwise across gene both genewise.
	"""
	
	bioc = "NewWave" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/NewWave_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/NewWave/NewWave_1.12.0.tar.gz"]

	version("1.12.0", md5="ed222f643c357c84a7eb8534aa7b3a91")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-sharedobject", type=("build", "run"))
