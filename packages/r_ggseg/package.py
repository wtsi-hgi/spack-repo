# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgseg(RPackage):
	"""Plotting Tool for Brain Atlases

	Contains 'ggplot2' geom for plotting brain atlases using 
    simple features. The largest component of the package is the data 
    for the two built-in atlases. Mowinckel & Vidal-Piñeiro (2020)
    <doi:10.1177/2515245920928009>.
	"""
	
	homepage = "https://github.com/ggseg/ggseg"
	cran = "ggseg" 

	version("1.6.5", md5="fd0307efcf9033f782efbbc46c48b81f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-sf@0.9.2:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
