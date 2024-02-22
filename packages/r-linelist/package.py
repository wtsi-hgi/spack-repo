# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinelist(RPackage):
	"""Tagging and Validating Epidemiological Data

	Provides tools to help storing and handling case line list data. The 'linelist' class adds a tagging system to classical 'data.frame' objects to identify key epidemiological data such as dates of symptom onset, epidemiological case definition, age, gender or disease outcome. Once tagged, these variables can be seamlessly used in downstream analyses, making data pipelines more robust and reliable. 
	"""
	
	homepage = "https://epiverse-trace.github.io/linelist/"
	cran = "linelist" 

	version("1.0.0", md5="1c31a21dee9b9c4a0ba0bb89ddd4844b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
