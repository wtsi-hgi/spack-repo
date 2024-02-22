# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowai(RPackage):
	"""Automatic and interactive quality control for flow cytometry data

	The package is able to perform an automatic or interactive quality control on FCS data acquired using flow cytometry instruments. By evaluating three different properties: 1) flow rate, 2) signal acquisition, 3) dynamic range, the quality control enables the detection and removal of anomalies.
	"""
	
	bioc = "flowAI" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowAI_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowAI/flowAI_1.32.0.tar.gz"]

	version("1.32.0", md5="714cb015ac01ee026e02fc24536770e5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
