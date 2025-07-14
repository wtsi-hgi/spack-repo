# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSc3(RPackage):
	"""Single-Cell Consensus Clustering

	A tool for unsupervised clustering and analysis of single cell RNA-Seq data.
	"""
	
	homepage = "https://github.com/hemberg-lab/SC3"
	bioc = "SC3" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SC3_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SC3/SC3_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="cf002839ce5fb3240d887d94dd81b8c6f88dcd94e31e7692720faaee8734b014", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SC3_1.30.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap@1.0.8:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
