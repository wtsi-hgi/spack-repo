# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCainterprtools(RPackage):
	"""Graphical Aid in Correspondence Analysis Interpretation and
Significance Testings

	Allows to plot a number of information related to the interpretation of Correspondence Analysis' results. It provides the facility to plot the contribution of rows and columns categories to the principal dimensions, the quality of points display on selected dimensions, the correlation of row and column categories to selected dimensions, etc. It also allows to assess which dimension(s) is important for the data structure interpretation by means of different statistics and tests. The package also offers the facility to plot the permuted distribution of the table total inertia as well as of the inertia accounted for by pairs of selected dimensions. Different facilities are also provided that aim to produce interpretation-oriented scatterplots. Reference: Alberti 2015 <doi:10.1016/j.softx.2015.07.001>.
	"""
	
	cran = "CAinterprTools" 

	version("1.1.0", md5="000316b5d5cc47035a4631b09d7fd807")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ca@0.70:", type=("build", "run"))
	depends_on("r-classint@0.2.3:", type=("build", "run"))
	depends_on("r-cluster@2.0.7:", type=("build", "run"))
	depends_on("r-factominer@1.40:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-hmisc@4.1.1:", type=("build", "run"))
	depends_on("r-rcmdrmisc@1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
