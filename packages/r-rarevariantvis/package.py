# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarevariantvis(RPackage):
	"""A suite for analysis of rare genomic variants in whole genome sequencing data

	Second version of RareVariantVis package aims to provide comprehensive information about rare variants for your genome data. It annotates, filters and presents genomic variants (especially rare ones) in a global, per chromosome way. For discovered rare variants CRISPR guide RNAs are designed, so the user can plan further functional studies. Large structural variants, including copy number variants are also supported. Package accepts variants directly from variant caller - for example GATK or Speedseq. Output of package are lists of variants together with adequate visualization. Visualization of variants is performed in two ways - standard that outputs png figures and interactive that uses JavaScript d3 package. Interactive visualization allows to analyze trio/family data, for example in search for causative variants in rare Mendelian diseases, in point-and-click interface. The package includes homozygous region caller and allows to analyse whole human genomes in less than 30 minutes on a desktop computer. RareVariantVis disclosed novel causes of several rare monogenic disorders, including one with non-coding causative variant - keratolythic winter erythema.
	"""
	
	bioc = "RareVariantVis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RareVariantVis_2.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RareVariantVis/RareVariantVis_2.30.0.tar.gz"]

	version("2.30.0", sha256="59d6a9c447ad649d107635413ba1df64dd7cfe578e605834183fd0461b61e257")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-phastcons100way-ucsc-hg19", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicscores", type=("build", "run"))
