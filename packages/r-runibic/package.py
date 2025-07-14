# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunibic(RPackage):
	"""runibic: row-based biclustering algorithm for analysis of gene expression data in R

	This package implements UbiBic algorithm in R. This biclustering algorithm for analysis of gene expression data was introduced by Zhenjia Wang et al. in 2016. It is currently considered the most promising biclustering method for identification of meaningful structures in complex and noisy data.
	"""
	
	homepage = "http://github.com/athril/runibic"
	bioc = "runibic" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/runibic_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/runibic/runibic_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="0db39adb3aebc4a0f26ac8fa38ac04addcadb56ad7b68ab4023ed6374d957766")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
