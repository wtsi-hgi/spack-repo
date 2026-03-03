# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelview(RPackage):
	"""Visualizing Panel Data

	Visualizes panel data. It has three main functionalities: (1) it plots the treatment status and missing values in a panel dataset; (2) it visualizes the temporal dynamics of a main variable of interest; (3) it depicts the bivariate relationships between a treatment variable and an outcome variable either by unit or in aggregate. For details, see <doi:10.18637/jss.v107.i07>.
	"""
	
	homepage = "https://yiqingxu.org/packages/panelview/index.html"
	cran = "panelView" 

	version("1.1.17", md5="6351dbbacad7852f2972f16930528ddf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
