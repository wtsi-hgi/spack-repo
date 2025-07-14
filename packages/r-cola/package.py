# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCola(RPackage):
	"""A Framework for Consensus Partitioning

	Subgroup classification is a basic task in genomic data analysis, especially for gene expression and DNA methylation data analysis. It can also be used to test the agreement to known clinical annotations, or to test whether there exist significant batch effects. The cola package provides a general framework for subgroup classification by consensus partitioning. It has the following features: 1. It modularizes the consensus partitioning processes that various methods can be easily integrated. 2. It provides rich visualizations for interpreting the results. 3. It allows running multiple methods at the same time and provides functionalities to straightforward compare results. 4. It provides a new method to extract features which are more efficient to separate subgroups. 5. It automatically generates detailed reports for the complete analysis. 6. It allows applying consensus partitioning in a hierarchical manner.
	"""
	
	homepage = "https://github.com/jokergoo/cola"
	bioc = "cola" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cola_2.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cola/cola_2.8.0.tar.gz"]

    version("2.14.0", tag="RELEASE_3_21")
	version("2.8.0", sha256="c4c3220dfdcc29df2d0da530bcefb0ffecf4ef3ecf258022176734100d303073")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-complexheatmap@2.5.4:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-circlize@0.4.7:", type=("build", "run"))
	depends_on("r-globaloptions@0.1:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-skmeans", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-knitr@1.4:", type=("build", "run"))
	depends_on("r-markdown@1.6:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-eulerr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
