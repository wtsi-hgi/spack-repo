# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactr(RPackage):
	"""Functional Annotation of Custom Transcriptomes

	factR contain tools to process and interact with custom-assembled transcriptomes (GTF). At its core, factR constructs CDS information on custom transcripts and subsequently predicts its functional output. In addition, factR has tools capable of plotting transcripts, correcting chromosome and gene information and shortlisting new transcripts.
	"""
	
	homepage = "https://fursham-h.github.io/factR/"
	bioc = "factR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/factR_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/factR/factR_1.4.0.tar.gz"]

	version("1.4.0", sha256="bb37f5dfd3ff46d37ff4ae979b5cb6753d953372522fac7e740f3869313e99e4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocgenerics@0.46:", type=("build", "run"))
	depends_on("r-biostrings@2.68:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.36:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.52:", type=("build", "run"))
	depends_on("r-genomicranges@1.52:", type=("build", "run"))
	depends_on("r-iranges@2.34:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rtracklayer@1.60:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-biocparallel@1.34:", type=("build", "run"))
	depends_on("r-s4vectors@0.38:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.2:", type=("build", "run"))
	depends_on("r-wiggleplotr@1.24:", type=("build", "run"))
	depends_on("r-rcurl@1.98:", type=("build", "run"))
	depends_on("r-xml@3.99:", type=("build", "run"))
	depends_on("r-drawproteins@1.20:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-pbapply@1.7:", type=("build", "run"))
	depends_on("r-crayon@1.5:", type=("build", "run"))
