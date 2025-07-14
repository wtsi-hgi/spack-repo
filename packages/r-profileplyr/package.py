# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfileplyr(RPackage):
	"""Visualization and annotation of read signal over genomic ranges with profileplyr

	Quick and straightforward visualization of read signal over genomic intervals is key for generating hypotheses from sequencing data sets (e.g. ChIP-seq, ATAC-seq, bisulfite/methyl-seq). Many tools both inside and outside of R and Bioconductor are available to explore these types of data, and they typically start with a bigWig or BAM file and end with some representation of the signal (e.g. heatmap). profileplyr leverages many Bioconductor tools to allow for both flexibility and additional functionality in workflows that end with visualization of the read signal.
	"""
	
	bioc = "profileplyr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/profileplyr_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/profileplyr/profileplyr_1.18.0.tar.gz"]

    version("1.24.1", tag="RELEASE_3_21")
	version("1.18.0", sha256="db9efeae6afec2121e6cec9152aaccd047a0d31d3abed3711cddd5b00a25cfb2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-soggi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-chipseeker", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm10-knowngene", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm9-knowngene", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-rgreat", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-enrichedheatmap", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
