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

	version("1.22.0", commit="9d50b974f02b155e618926f9f8501a9d16e01f78")
	version("1.16.0", commit="5122b11cbf5ce2e471e6f989fb126af47d906a47")

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
