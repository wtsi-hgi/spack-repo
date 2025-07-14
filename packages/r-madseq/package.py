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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MADSEQ_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MADSEQ/MADSEQ_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="dd23424c3391e22bbc11136e19240c9ff7e49f4d4f35887eb589021a7e926f81")

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
