# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgperiodic(RPackage):
	"""Easy Plotting of Periodic Data with 'ggplot2'

	Implements methods to plot periodic data in any arbitrary range on the fly.
	"""
	
	homepage = "https://github.com/eliocamp/ggperiodic"
	cran = "ggperiodic" 

	version("1.0.3", md5="f16c8619cda34ff90e5791d7fc533972")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sticky", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
