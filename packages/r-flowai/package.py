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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowAI_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowAI/flowAI_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="7ffe8ec5e2736ad644cc24174b6350a5bd9f382086ea70a2a2c78883911b21ae")

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
