# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtsfilter(RPackage):
	"""Filter replicated high-throughput transcriptome sequencing data

	This package implements a filtering procedure for replicated transcriptome sequencing data based on a global Jaccard similarity index in order to identify genes with low, constant levels of expression across one or more experimental conditions.
	"""
	
	bioc = "HTSFilter" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HTSFilter_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HTSFilter/HTSFilter_1.42.0.tar.gz"]

	version("1.42.0", md5="6eb5ebe090ac02b5a0099f63f3e6ccc6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
