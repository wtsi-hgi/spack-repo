# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeedmatchr(RPackage):
	"""Find Matches to Canonical SiRNA Seeds in Genomic Features

	On-target gene knockdown using siRNA ideally results from binding 
    fully complementary regions in mRNA transcripts to induce cleavage. 
    Off-target siRNA gene knockdown can occur through several modes, one being 
    a seed-mediated mechanism mimicking miRNA gene regulation. Seed-mediated 
    off-target effects occur when the ~8 nucleotides at the 5’ end of the guide 
    strand, called a seed region, bind the 3’ untranslated regions of mRNA, 
    causing reduced translation. Experiments using siRNA knockdown paired with 
    RNA-seq can be used to detect siRNA sequences with potential off-target 
    effects driven by the seed region. 'SeedMatchR' provides tools for exploring 
    and detecting potential seed-mediated off-target effects of siRNA in RNA-seq 
    experiments. 'SeedMatchR' is designed to extend current differential 
    expression analysis tools, such as 'DESeq2', by annotating results with 
    predicted seed matches. Using publicly available data, we demonstrate the 
    ability of 'SeedMatchR' to detect cumulative changes in differential gene 
    expression attributed to siRNA seed regions. 
	"""
	
	homepage = "https://tacazares.github.io/SeedMatchR/"
	cran = "SeedMatchR" 

	version("1.1.1", md5="b7fc4c6bd9f012555592bda1755c87ec")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggmsa", type=("build", "run"))
	depends_on("r-msa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
