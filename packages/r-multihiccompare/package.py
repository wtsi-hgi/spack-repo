# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultihiccompare(RPackage):
	"""Normalize and detect differences between Hi-C datasets when replicates of each experimental condition are available

	multiHiCcompare provides functions for joint normalization and difference detection in multiple Hi-C datasets. This extension of the original HiCcompare package now allows for Hi-C experiments with more than 2 groups and multiple samples per group. multiHiCcompare operates on processed Hi-C data in the form of sparse upper triangular matrices. It accepts four column (chromosome, region1, region2, IF) tab-separated text files storing chromatin interaction matrices. multiHiCcompare provides cyclic loess and fast loess (fastlo) methods adapted to jointly normalizing Hi-C data. Additionally, it provides a general linear model (GLM) framework adapting the edgeR package to detect differences in Hi-C data in a distance dependent manner.
	"""
	
	homepage = "https://github.com/dozmorovlab/multiHiCcompare"
	bioc = "multiHiCcompare" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/multiHiCcompare_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/multiHiCcompare/multiHiCcompare_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="6b4cf113ae308b818ff7f695b80a1fa6025f95d394dafb855754e4409c305094")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hiccompare", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-genomeinfodbdata", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-aggregation", type=("build", "run"))
