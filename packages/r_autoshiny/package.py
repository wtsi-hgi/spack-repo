# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoshiny(RPackage):
	"""Automatic Transformation of an 'R' Function into a 'shiny' App

	Static code compilation of a 'shiny' app given an R function (into 'ui.R' and 'server.R' files or into a 'shiny' app object). See examples at <https://github.com/alekrutkowski/autoshiny>.
	"""
	
	homepage = "https://github.com/alekrutkowski/autoshiny"
	cran = "autoshiny" 

	version("0.0.3", md5="026f237c1322c29085f9f2e1fb93b500")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
