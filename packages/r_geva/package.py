# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeva(RPackage):
	"""Gene Expression Variation Analysis (GEVA)

	Statistic methods to evaluate variations of differential expression (DE) between multiple biological conditions. It takes into account the fold-changes and p-values from previous differential expression (DE) results that use large-scale data (*e.g.*, microarray and RNA-seq) and evaluates which genes would react in response to the distinct experiments. This evaluation involves an unique pipeline of statistical methods, including weighted summarization, quantile detection, cluster analysis, and ANOVA tests, in order to classify a subset of relevant genes whose DE is similar or dependent to certain biological factors.
	"""
	
	homepage = "https://github.com/sbcblab/geva"
	bioc = "geva" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/geva_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/geva/geva_1.10.0.tar.gz"]

	version("1.10.0", md5="ac06c7a9df29f5eb16fe102c81369ccb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
