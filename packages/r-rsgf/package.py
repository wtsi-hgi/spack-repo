# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsgf(RPackage):
	"""SGF (Smart Game File) File Format Import

	Import SGF (Smart Game File) into R.
	"""
	
	cran = "Rsgf" 

	version("1.0.0", md5="e0a925df03199c28337d4ee073d597c0")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
