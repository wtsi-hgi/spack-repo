# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsea(RPackage):
	"""IP-seq data analysis and vizualization

	qsea (quantitative sequencing enrichment analysis) was developed as the successor of the MEDIPS package for analyzing data derived from methylated DNA immunoprecipitation (MeDIP) experiments followed by sequencing (MeDIP-seq). However, qsea provides several functionalities for the analysis of other kinds of quantitative sequencing data (e.g. ChIP-seq, MBD-seq, CMS-seq and others) including calculation of differential enrichment between groups of samples.
	"""
	
	bioc = "qsea" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/qsea_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/qsea/qsea_1.28.0.tar.gz"]

	version("1.28.0", md5="2891ba342f17500cee6391d1f388c3c4")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-hmmcopy", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
