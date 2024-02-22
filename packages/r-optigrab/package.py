# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptigrab(RPackage):
	"""Command-Line Parsing for an R World

	Parse options from the command-line using a simple, clean syntax. 
    It requires little or no specification and supports short and long options,
    GNU-, Java- or Microsoft- style syntaxes, verb commands and more. 
	"""
	
	homepage = "https://github.com/decisionpatterns/optigrab"
	cran = "optigrab" 

	version("0.9.2.1", md5="67abdadef8ff78b342002b99947e2326")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringi@0.4.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
