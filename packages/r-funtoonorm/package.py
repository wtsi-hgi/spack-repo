# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuntoonorm(RPackage):
	"""Normalization Procedure for Infinium HumanMethylation450 BeadChip Kit

	Provides a function to normalize Illumina Infinium Human Methylation 450 BeadChip (Illumina 450K), correcting for tissue and/or cell type.
	"""
	
	bioc = "funtooNorm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/funtooNorm_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/funtooNorm/funtooNorm_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="fe016d48aa1d1f565d2b783ee20a4068a123548c393ef3c7bea582608d92ddbc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
