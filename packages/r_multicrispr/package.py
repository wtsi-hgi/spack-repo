# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticrispr(RPackage):
	"""Multi-locus multi-purpose Crispr/Cas design

	This package is for designing Crispr/Cas9 and Prime Editing experiments. It contains functions to (1) define and transform genomic targets, (2) find spacers (4) count offtarget (mis)matches, and (5) compute Doench2016/2014 targeting efficiency. Care has been taken for multicrispr to scale well towards large target sets, enabling the design of large Crispr/Cas9 libraries.
	"""
	
	homepage = "https://github.com/loosolab/multicrispr"
	bioc = "multicrispr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/multicrispr_1.12.9.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/multicrispr/multicrispr_1.12.9.tar.gz"]

	version("1.12.9", md5="1eb85739f11d9bac705ffb44aa5cc541")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-crisprseek", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-karyoploter", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-rbowtie", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-assertive-reflection", type=("build", "link", "run"))
