# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagar(RPackage):
	"""MAGAR: R-package to compute methylation Quantitative Trait Loci (methQTL) from DNA methylation and genotyping data

	"Methylation-Aware Genotype Association in R" (MAGAR) computes methQTL from DNA methylation and genotyping data from matched samples. MAGAR uses a linear modeling stragety to call CpGs/SNPs that are methQTLs. MAGAR accounts for the local correlation structure of CpGs.
	"""
	
	homepage = "https://github.com/MPIIComputationalEpigenetics/MAGAR"
	bioc = "MAGAR"

	version("1.16.0", commit="4b8bf4852f1d04a54da727ac710633dfee314e86")
	version("1.10.0", commit="b2f223aa6df854e6690bf635f85ef31e45dd4ef2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rnbeads", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-crlmm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-bigstatsr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-argparse", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-rnbeads-hg19", type=("build", "run"))
