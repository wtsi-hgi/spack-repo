# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFluentgenomics(RPackage):
	"""A plyranges and tximeta workflow

	An extended workflow using the plyranges and tximeta packages for fluent genomic data analysis. Use tximeta to correctly import RNA-seq transcript quantifications and summarize them to gene counts for downstream analysis. Use plyranges for clearly expressing operations over genomic coordinates and to combine results from differential expression and differential accessibility analyses.
	"""
	
	homepage = "https://github.com/sa-lee/fluentGenomics"
	bioc = "fluentGenomics" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/fluentGenomics_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/fluentGenomics/fluentGenomics_1.14.0.tar.gz"]

	version("1.14.0", md5="e7607b73ea44cc70d2173218a73561e5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plyranges@1.7.7:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))

