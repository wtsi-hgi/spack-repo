# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvaluomer(RPackage):
	"""Evaluation of Bioinformatics Metrics

	Evaluating the reliability of your own metrics and the measurements done on your own datasets by analysing the stability and goodness of the classifications of such metrics.
	"""
	
	homepage = "https://github.com/neobernad/evaluomeR"
	bioc = "evaluomeR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/evaluomeR_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/evaluomeR/evaluomeR_1.18.0.tar.gz"]

	version("1.18.0", md5="2cee372b9bb28916d6ab543be8eca9b2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-cluster@2.0.9:", type=("build", "run"))
	depends_on("r-fpc@2.2.3:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
	depends_on("r-flexmix@2.3.15:", type=("build", "run"))
	depends_on("r-corrplot@0.84:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-prabclus", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
