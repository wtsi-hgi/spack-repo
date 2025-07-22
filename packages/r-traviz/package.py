# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraviz(RPackage):
	"""Trajectory functions for visualization and interpretation.

	traviz provides a suite of functions to plot trajectory related objects from Bioconductor packages. It allows plotting trajectories in reduced dimension, as well as averge gene expression smoothers as a function of pseudotime. Asides from general utility functions, traviz also allows plotting trajectories estimated by Slingshot, as well as smoothers estimated by tradeSeq. Furthermore, it allows for visualization of Slingshot trajectories using ggplot2.
	"""
	
	bioc = "traviz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/traviz_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/traviz/traviz_1.8.0.tar.gz"]

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="6682a3ace8eab64755f34a77a399ca677f1c87acbcc4c3d77e9d03408656c079")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-slingshot", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
