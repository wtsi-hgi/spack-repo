# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigoptr(RPackage):
	"""R API Wrapper for SigOpt

	Interfaces with the 'SigOpt' API. More info at <https://sigopt.com>.
	"""
	
	cran = "SigOptR" 

	version("0.0.1", md5="f72713965f495d11d0330847c261510d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
