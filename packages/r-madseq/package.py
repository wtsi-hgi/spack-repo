# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadseq(RPackage):
	"""Mosaic Aneuploidy Detection and Quantification using Massive Parallel Sequencing Data

	The MADSEQ package provides a group of hierarchical Bayeisan models for the detection of mosaic aneuploidy, the inference of the type of aneuploidy and also for the quantification of the fraction of aneuploid cells in the sample.
	"""
	
	homepage = "https://github.com/ykong2/MADSEQ"
	bioc = "MADSEQ"

	version("1.34.0", commit="2ba7c5f729f7847a8e3c34fe3c8a44e201436e95")
	version("1.28.0", commit="24480264d8dcf71e5a9f9eb73dd01c838c31018c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
