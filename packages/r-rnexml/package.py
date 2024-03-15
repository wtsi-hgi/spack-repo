# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnexml(RPackage):
	"""Semantically Rich I/O for the 'NeXML' Format.

	Provides access to phyloinformatic data in 'NeXML' format. The package
	should add new functionality to R such as the possibility to manipulate
	'NeXML' objects in more various and refined way and compatibility with
	'ape' objects."""

	cran = "RNeXML"

	version("2.4.11", md5="7901174d10570464473f7445ec8fee78")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape@3.1:", type=("build", "run"))
	depends_on("r-xml@3.95:", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
	depends_on("r-reshape2@1.2.2:", type=("build", "run"))
	depends_on("r-httr@0.3:", type=("build", "run"))
	depends_on("r-uuid@0.1.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tidyr@0.3.1:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
