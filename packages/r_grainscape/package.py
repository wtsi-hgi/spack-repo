# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrainscape(RPackage):
	"""Landscape Connectivity, Habitat, and Protected Area Networks

	Given a landscape resistance surface, creates minimum planar graph
    (Fall et al. (2007) <doi:10.1007/s10021-007-9038-7>) and grains of connectivity
    (Galpern et al. (2012) <doi:10.1111/j.1365-294X.2012.05677.x>) models that can be
    used to calculate effective distances for landscape connectivity at multiple scales.
    Documentation is provided by several vignettes, and a paper
    (Chubaty, Galpern & Doctolero (2020) <doi:10.1111/2041-210X.13350>).
	"""
	
	homepage = "https://www.alexchubaty.com/grainscape/"
	cran = "grainscape" 

	version("0.4.4", md5="1a1dd2765d7da1854aa8e858e6048752")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
