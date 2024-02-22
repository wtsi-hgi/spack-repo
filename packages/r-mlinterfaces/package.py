# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlinterfaces(RPackage):
	"""Uniform interfaces to R machine learning procedures for data in
	Bioconductor containers.

	This package provides uniform interfaces to machine learning code for
	data in R and Bioconductor containers."""

	bioc = "MLInterfaces"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MLInterfaces_1.82.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MLInterfaces/MLInterfaces_1.82.0.tar.gz"]

	version("1.82.0", md5="acb5f91abaa05ef8c6b156b2cc7df846")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.11:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-ggvis", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-threejs@0.2.2:", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
