# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSweidnumbr(RPackage):
	"""Handling of Swedish Identity Numbers

	Structural handling of identity numbers used in the Swedish
    administration such as personal identity numbers ('personnummer') and
    organizational identity numbers ('organisationsnummer').
	"""
	
	homepage = "https://github.com/rOpenGov/sweidnumbr"
	cran = "sweidnumbr" 

	version("1.5.0", md5="52d3ba03ce903a4da73377421f690487")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lubridate@1.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
