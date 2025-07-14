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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methylCC_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methylCC/methylCC_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="1caeea2cbf70dbfd73a4a4f1a67d5fe2b690dfc45c84f7e54085c43750332bbf")

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
