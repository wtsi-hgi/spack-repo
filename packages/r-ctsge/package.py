# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtsge(RPackage):
	"""Clustering of Time Series Gene Expression data

	Methodology for supervised clustering of potentially many predictor variables, such as genes etc., in time series datasets Provides functions that help the user assigning genes to predefined set of model profiles.
	"""
	
	homepage = "https://github.com/michalsharabi/ctsGE"
	bioc = "ctsGE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ctsGE_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ctsGE/ctsGE_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="278942630487033bb67b94525e97240ab2f5f17b6833d654a69e521cef4135bc")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ccapp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
