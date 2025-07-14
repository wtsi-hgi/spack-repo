# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaddr(RPackage):
	"""Statistical tests for detecting differential distributions based on the 2-Wasserstein distance

	The package offers statistical tests based on the 2-Wasserstein distance for detecting and characterizing differences between two distributions given in the form of samples. Functions for calculating the 2-Wasserstein distance and testing for differential distributions are provided, as well as a specifically tailored test for differential expression in single-cell RNA sequencing data.
	"""
	
	homepage = "https://github.com/goncalves-lab/waddR.git"
	bioc = "waddR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/waddR_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/waddR/waddR_1.16.0.tar.gz"]

	version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="675e24e4135651c3b0618452334769d5388f21a45979acd82fd1f6b84bbf451d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-arm@1.10.1:", type=("build", "run"))
	depends_on("r-eva", type=("build", "run"))
	depends_on("r-biocfilecache@2.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
