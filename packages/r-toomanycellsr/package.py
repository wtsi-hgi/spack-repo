# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToomanycellsr(RPackage):
	"""An R Wrapper for 'TooManyCells'

	An R wrapper for using 'TooManyCells', a command line program for clustering, visualizing, and quantifying cell clade relationships. See <https://gregoryschwartz.github.io/too-many-cells/> for more details.
	"""
	
	cran = "TooManyCellsR" 

	version("0.1.1.0", md5="4da76d9150d4522ffa3717c15d61d219")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
