# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabomxtr(RPackage):
	"""A package to run mixture models for truncated metabolomics data with normal or lognormal distributions

	The functions in this package return optimized parameter estimates and log likelihoods for mixture models of truncated data with normal or lognormal distributions.
	"""
	
	bioc = "metabomxtr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metabomxtr_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metabomxtr/metabomxtr_1.36.0.tar.gz"]

	version("1.36.0", md5="ec247e3fe8099096d1bfcc8fff93f08d")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
