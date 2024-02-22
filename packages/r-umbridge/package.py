# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUmbridge(RPackage):
	"""Integration for the UM-Bridge Protocol

	A convenient wrapper for the UM-Bridge protocol. UM-Bridge is a protocol designed for coupling uncertainty quantification (or statistical / optimization) software to numerical models. A model is represented as a mathematical function with optional support for derivatives via Jacobian actions etc.
	"""
	
	cran = "umbridge" 

	version("1.0", md5="ac135ea79ae9ff0de6f1f5cbd194d937")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
