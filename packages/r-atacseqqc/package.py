# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtacseqqc(RPackage):
	"""ATAC-seq Quality Control

	ATAC-seq, an assay for Transposase-Accessible Chromatin using sequencing, is a rapid and sensitive method for chromatin accessibility analysis. It was developed as an alternative method to MNase-seq, FAIRE-seq and DNAse-seq. Comparing to the other methods, ATAC-seq requires less amount of the biological samples and time to process. In the process of analyzing several ATAC-seq dataset produced in our labs, we learned some of the unique aspects of the quality assessment for ATAC-seq data.To help users to quickly assess whether their ATAC-seq experiment is successful, we developed ATACseqQC package partially following the guideline published in Nature Method 2013 (Greenleaf et al.), including diagnostic plot of fragment size distribution, proportion of mitochondria reads, nucleosome positioning pattern, and CTCF or other Transcript Factor footprints.
	"""
	
	bioc = "ATACseqQC"

	version("1.32.0", commit="87b9b5129f308b58df33502ea4b3e1541bf2a7fb")
	version("1.26.0", commit="415dbcbf18b7e28e4d6dc4913a4446877600f0db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-chippeakanno", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicscores", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-motifstack", type=("build", "run"))
	depends_on("r-preseqr", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
