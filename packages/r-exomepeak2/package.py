# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExomepeak2(RPackage):
	"""Peak Calling and differential analysis for MeRIP-Seq

	exomePeak2 provides peak detection and differential methylation for Methylated RNA Immunoprecipitation Sequencing (MeRIP-Seq) data. MeRIP-Seq is a commonly applied sequencing assay that measures the location and abundance of RNA modification sites under specific cellular conditions. The technique is sensitive to PCR amplification biases commonly found in NGS data. In addition, the efficiency of immunoprecipitation often varies between different IP samples. exomePeak2 can perform peak calling and differential analysis independent of GC content bias and IP efficiency changes.
	"""
	
	bioc = "exomePeak2" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/exomePeak2_1.14.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/exomePeak2/exomePeak2_1.14.3.tar.gz"]

	version("1.14.3", sha256="f0d28b69ffc32ffdbb445e605c18a865692fa8debfd35619d84bd24d210a7fc3", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/exomePeak2_1.14.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-speedglm", type=("build", "run"))
