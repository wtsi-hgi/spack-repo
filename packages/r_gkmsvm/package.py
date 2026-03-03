# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGkmsvm(RPackage):
	"""Gapped-Kmer Support Vector Machine

	Imports the 'gkmSVM' v2.0 functionalities into R <https://www.beerlab.org/gkmsvm/>
    It also uses the 'kernlab' library (separate R package by different authors) for various SVM algorithms.
    Users should note that the suggested packages 'rtracklayer', 'GenomicRanges', 'BSgenome', 'BiocGenerics', 
    'Biostrings', 'GenomeInfoDb', 'IRanges', and 'S4Vectors' are all BioConductor packages <https://bioconductor.org>.
	"""
	
	cran = "gkmSVM" 

	version("0.83.0", md5="c385f4ce24103917110ed2c0c2a5f0a4")

	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
