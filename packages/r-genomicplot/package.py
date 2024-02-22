# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicplot(RPackage):
	"""Plot profiles of next generation sequencing data in genomic features

	Visualization of next generation sequencing (NGS) data is essential for interpreting high-throughput genomics experiment results. 'GenomicPlot' facilitates plotting of NGS data in various formats (bam, bed, wig and bigwig); both coverage and enrichment over input can be computed and displayed with respect to genomic features (such as UTR, CDS, enhancer), and user defined genomic loci or regions. Statistical tests on signal intensity within user defined regions of interest can be performed and represented as boxplots or bar graphs. Parallel processing is used to speed up computation on multicore platforms. In addition to genomic plots which is suitable for displaying of coverage of genomic DNA (such as ChIPseq data), metagenomic (without introns) plots can also be made for RNAseq or CLIPseq data as well.
	"""
	
	homepage = "https://github.com/shuye2009/GenomicPlot"
	bioc = "GenomicPlot" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GenomicPlot_1.0.4.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GenomicPlot/GenomicPlot_1.0.4.tar.gz"]

	version("1.0.4", md5="28964cfb6084eea62d3cb24b16e7b064")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-genomicranges@1.46.1:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rtracklayer@1.54:", type=("build", "run"))
	depends_on("r-plyranges@1.14:", type=("build", "run"))
	depends_on("r-cowplot@1.1.1:", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-rcas@1.20:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-genomicalignments@1.30:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggsignif@0.6.3:", type=("build", "run"))
	depends_on("r-ggsci@2.9:", type=("build", "run"))
	depends_on("r-genomation@1.26:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
