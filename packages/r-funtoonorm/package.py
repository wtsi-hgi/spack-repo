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

	version("1.32.0", commit="f0d035d0c242085accff66cf425a434808c7c301")
	version("1.26.0", commit="097b881169c2734f6fdc55811b88124d6a171c9c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
