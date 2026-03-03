# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotmelm(RPackage):
	"""Plot Marginal Effects from Linear Models

	Plot marginal effects for interactions estimated
    from linear models.
	"""
	
	cran = "plotMElm" 

	version("0.1.5", md5="0827f53fde8b378d97f7d64a0612a341")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-interactiontest", type=("build", "run"))
