# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataexplorer(RPackage):
	"""Automate Data Exploration and Treatment

	Automated data exploration process for analytic tasks and predictive modeling, so
    that users could focus on understanding data and extracting insights. The package scans and
    analyzes each variable, and visualizes them with typical graphical techniques. Common
    data processing methods are also available to treat and format data.
	"""
	
	homepage = "http://boxuancui.github.io/DataExplorer/"
	cran = "DataExplorer" 

	version("0.8.3", md5="0402014e1b2d468ca2b94a6f655c23a0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.13.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rmarkdown@2.5:", type=("build", "run"))
	depends_on("r-networkd3@0.4:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
