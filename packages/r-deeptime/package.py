# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeeptime(RPackage):
	"""Plotting Tools for Anyone Working in Deep Time

	Extends the functionality of other plotting packages like
    'ggplot2' and 'lattice' to help facilitate the plotting of data over long time
    intervals, including, but not limited to, geological, evolutionary, and ecological
    data. The primary goal of 'deeptime' is to enable users to add highly customizable
    timescales to their visualizations. Other functions are also included to assist
    with other areas of deep time visualization.
	"""
	
	homepage = "https://github.com/willgearty/deeptime"
	cran = "deeptime" 

	version("1.1.1", md5="9a8b54f8b22d4af384414a3a5319376b")
	version("1.0.1", md5="dc8668e067eed6a86eaa28eabea92c06")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-geomtextpath", type=("build", "run"))
