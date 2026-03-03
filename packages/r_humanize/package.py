# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanize(RPackage):
	"""Create Values for Human Consumption

	An almost direct port of the 'python' 'humanize' package <https://github.com/jmoiron/humanize>.
  This package contains utilities to convert values into human readable forms. 
	"""
	
	homepage = "https://newtux.github.io/humanize/index.html"
	cran = "humanize" 

	version("0.2.0", md5="8e081d29cafe7fc75d4f7e1c47284e43")

	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
