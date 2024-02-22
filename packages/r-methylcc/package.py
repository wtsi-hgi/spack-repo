# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylcc(RPackage):
	"""Estimate the cell composition of whole blood in DNA methylation samples

	A tool to estimate the cell composition of DNA methylation whole blood sample measured on any platform technology (microarray and sequencing).
	"""
	
	homepage = "https://github.com/stephaniehicks/methylCC/"
	bioc = "methylCC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/methylCC_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/methylCC/methylCC_1.16.0.tar.gz"]

	version("1.16.0", md5="77566e7338f615ca5305d6e00465908b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-flowsorted-blood-450k", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
