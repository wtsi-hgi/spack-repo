# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowcatchr(RPackage):
	"""Tools to analyze in vivo microscopy imaging data focused on tracking flowing blood cells

	flowcatchR is a set of tools to analyze in vivo microscopy imaging data, focused on tracking flowing blood cells. It guides the steps from segmentation to calculation of features, filtering out particles not of interest, providing also a set of utilities to help checking the quality of the performed operations (e.g. how good the segmentation was). It allows investigating the issue of tracking flowing cells such as in blood vessels, to categorize the particles in flowing, rolling and adherent. This classification is applied in the study of phenomena such as hemostasis and study of thrombosis development. Moreover, flowcatchR presents an integrated workflow solution, based on the integration with a Shiny App and Jupyter notebooks, which is delivered alongside the package, and can enable fully reproducible bioimage analysis in the R environment.
	"""
	
	homepage = "https://github.com/federicomarini/flowcatchR"
	bioc = "flowcatchR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowcatchR_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowcatchR/flowcatchR_1.36.0.tar.gz"]

	version("1.36.0", sha256="c6579e5baa75944b20b4ca2e8e0a78ebc3c14b3feefed944b1119450585ce47a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
