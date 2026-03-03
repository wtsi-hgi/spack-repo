# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenstats(RPackage):
	"""A Robust and Scalable Software Package for Reproducible Analysis of High-Throughput genotype-phenotype association

	Package contains several methods for statistical analysis of genotype to phenotype association in high-throughput screening pipelines.
	"""
	
	homepage = "https://git.io/Jv5w0"
	bioc = "OpenStats" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OpenStats_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OpenStats/OpenStats_1.14.0.tar.gz"]

	version("1.14.0", md5="0e8a0fcd25ca1377c5bce5068bfaabff")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-aiccmodavg", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-summarytools", type=("build", "run"))
