# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColordistance(RPackage):
	"""Distance Metrics for Image Color Similarity

	Loads and displays images, selectively masks specified background
    colors, bins pixels by color using either data-dependent or
    automatically generated color bins, quantitatively measures color
    similarity among images using one of several distance metrics for
    comparing pixel color clusters, and clusters images by object color
    similarity. Uses CIELAB, RGB, or HSV color spaces. Originally written
    for use with organism coloration (reef fish color diversity, butterfly
    mimicry, etc), but easily applicable for any image set.
	"""
	
	cran = "colordistance" 

	version("1.1.2", md5="228209bb610143a0b9105c0accdfe927")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-emdist", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
