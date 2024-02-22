# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfm(RPackage):
	"""Atomic Force Microscope Image Analysis

	Provides Atomic Force Microscope images analysis such as Gaussian mixes identification, Power
    Spectral Density, roughness against lengthscale, experimental variogram and variogram models,
    fractal dimension and scale, 2D network analysis. The AFM images can be exported to STL format for 3D
    printing.
	"""
	
	cran = "AFM" 

	version("2.0", md5="badd25d2dabc13948abb63340157aa55")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-gstat@1.0.26:", type=("build", "run"))
	depends_on("r-fractaldim@0.8.4:", type=("build", "run"))
	depends_on("r-rgl@0.96:", type=("build", "run"))
	depends_on("r-pracma@1.8.6:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-sp@1.2.0:", type=("build", "run"))
	depends_on("r-png@0.1.7:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-shiny@0.12.2:", type=("build", "run"))
	depends_on("r-shinyjs@0.4:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-dbscan@0.9.8:", type=("build", "run"))
	depends_on("r-mixtools@1.0.4:", type=("build", "run"))
	depends_on("r-fftwtools@0.9.8:", type=("build", "run"))
