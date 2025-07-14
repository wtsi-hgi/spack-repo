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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggcyto_1.30.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggcyto/ggcyto_1.30.2.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.2", sha256="f63c3019a2702a94f8d34e5169093aa24a6f08b7a5e1d87b2ee3faabcc1ae245")
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
