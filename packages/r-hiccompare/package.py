# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiccompare(RPackage):
	"""HiCcompare: Joint normalization and comparative analysis of multiple Hi-C datasets

	HiCcompare provides functions for joint normalization and difference detection in multiple Hi-C datasets. HiCcompare operates on processed Hi-C data in the form of chromosome-specific chromatin interaction matrices. It accepts three-column tab-separated text files storing chromatin interaction matrices in a sparse matrix format which are available from several sources. HiCcompare is designed to give the user the ability to perform a comparative analysis on the 3-Dimensional structure of the genomes of cells in different biological states.`HiCcompare` differs from other packages that attempt to compare Hi-C data in that it works on processed data in chromatin interaction matrix format instead of pre-processed sequencing data. In addition, `HiCcompare` provides a non-parametric method for the joint normalization and removal of biases between two Hi-C datasets for the purpose of comparative analysis. `HiCcompare` also provides a simple yet robust method for detecting differences between Hi-C datasets.
	"""
	
	homepage = "https://github.com/dozmorovlab/HiCcompare"
	bioc = "HiCcompare" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HiCcompare_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HiCcompare/HiCcompare_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="4dbca074754c4aea7f95e1a4483943d955fa7584b69d37865a90ffde7edb68ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
