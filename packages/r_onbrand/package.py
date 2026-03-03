# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnbrand(RPackage):
	"""Templated Reporting Workflows in Word and PowerPoint

	Automated reporting in Word and PowerPoint can require customization for each organizational template. This package works around this by adding standard reporting functions and an abstraction layer to facilitate automated reporting workflows that can be replicated across different organizational templates.
	"""
	
	homepage = "https://onbrand.ubiquity.tools/"
	cran = "onbrand" 

	version("1.0.5", md5="955429cd1e23da99e278e5691faa03fd")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-officer@0.3.7:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
