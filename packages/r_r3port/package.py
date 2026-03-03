# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR3port(RPackage):
	"""Report Functions to Create HTML and PDF Files

	Create and combine HTML and PDF reports from within R.
    Possibility to design tables and listings for reporting and also include R plots.
	"""
	
	homepage = "https://github.com/RichardHooijmaijers/R3port"
	cran = "R3port" 

	version("0.2.5", md5="3223b32109af196fde91bf2a6d851dc2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-tinytex", type=("build", "run"))
