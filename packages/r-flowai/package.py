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

	version("1.38.0", commit="129ff536c26e14a04dbda8369e015203441d7829")
	version("1.32.0", commit="2610f69e58d70237bec559105d240921e7218095")

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
