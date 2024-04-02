# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmappr2(RPackage):
	"""Mutation Mapping Analysis Pipeline for Pooled RNA-Seq

	MMAPPR2 maps mutations resulting from pooled RNA-seq data from the F2 cross of forward genetic screens. Its predecessor is described in a paper published in Genome Research (Hill et al. 2013). MMAPPR2 accepts aligned BAM files as well as a reference genome as input, identifies loci of high sequence disparity between the control and mutant RNA sequences, predicts variant effects using Ensembl's Variant Effect Predictor, and outputs a ranked list of candidate mutations.
	"""
	
	homepage = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613585/"
	bioc = "MMAPPR2" 

	version("1.16.0", commit="e30fb29d0061925a94f95a6a23881605290ddcd2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ensemblvep@1.20:", type=("build", "run"))
	depends_on("r-gmapr", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-varianttools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("ensembl-vep", type=("build", "link", "run"))
	depends_on("samtools", type=("build", "link", "run"))
