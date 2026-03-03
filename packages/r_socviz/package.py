# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSocviz(RPackage):
	"""Utility Functions and Data Sets for Data Visualization

	Supporting materials for a course and book on data visualization. It contains utility functions for graphs and several sample data sets. See Healy (2019) <ISBN 978-0691181622>.
	"""
	
	homepage = "http://kjhealy.github.io/socviz/"
	cran = "socviz" 

	version("1.2", md5="cef7a4669cadb07178474ff0fce5c1ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
