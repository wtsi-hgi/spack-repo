# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVimps(RPackage):
	"""Calculate Variable Importance with Knock Off Variables

	The variable importance is calculated using knock off variables. Then output can be provided in numerical and graphical form. Meredith L Wallace (2023) <doi:10.1186/s12874-023-01965-x>.
	"""
	
	cran = "VIMPS" 

	version("1.0", md5="e236fa8e5ac75bdebcd64cb2735a0b9d")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-knockoff", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
