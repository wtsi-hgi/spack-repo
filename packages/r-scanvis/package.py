# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanvis(RPackage):
	"""SCANVIS - a tool for SCoring, ANnotating and VISualizing splice junctions

	SCANVIS is a set of annotation-dependent tools for analyzing splice junctions and their read support as predetermined by an alignment tool of choice (for example, STAR aligner). SCANVIS assesses each junction's relative read support (RRS) by relating to the context of local split reads aligning to annotated transcripts. SCANVIS also annotates each splice junction by indicating whether the junction is supported by annotation or not, and if not, what type of junction it is (e.g. exon skipping, alternative 5' or 3' events, Novel Exons). Unannotated junctions are also futher annotated by indicating whether it induces a frame shift or not. SCANVIS includes a visualization function to generate static sashimi-style plots depicting relative read support and number of split reads using arc thickness and arc heights, making it easy for users to spot well-supported junctions. These plots also clearly delineate unannotated junctions from annotated ones using designated color schemes, and users can also highlight splice junctions of choice. Variants and/or a read profile are also incoroporated into the plot if the user supplies variants in bed format and/or the BAM file. One further feature of the visualization function is that users can submit multiple samples of a certain disease or cohort to generate a single plot - this occurs via a "merge" function wherein junction details over multiple samples are merged to generate a single sashimi plot, which is useful when contrasting cohorots (eg. disease vs control).
	"""
	
	bioc = "SCANVIS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SCANVIS_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SCANVIS/SCANVIS_1.16.0.tar.gz"]

	version("1.16.0", md5="36977f903eb019d8171d60519360cd9e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
