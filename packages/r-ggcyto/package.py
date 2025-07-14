# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgcyto(RPackage):
	"""Visualize Cytometry data with ggplot

	With the dedicated fortify method implemented for flowSet, ncdfFlowSet and GatingSet classes, both raw and gated flow cytometry data can be plotted directly with ggplot. ggcyto wrapper and some customed layers also make it easy to add gates and population statistics to the plot.
	"""
	
	homepage = "https://github.com/RGLab/ggcyto/issues"
	bioc = "ggcyto"

	version("1.36.0", commit="e022e6cbd6bcf4f9e4e14a5f7fc94c1dd2fb4199")
	version("1.30.2", commit="ea5c74d4c2733713963eaddb6d789b972cabf9a5")
	version("1.30.0", md5="f50828f54e40b73d30aa3ac0ef06de21")

	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-flowcore@1.41.5:", type=("build", "run"))
	depends_on("r-ncdfflow@2.17.1:", type=("build", "run"))
	depends_on("r-flowworkspace@4.3.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
