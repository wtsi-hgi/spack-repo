# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3viz(RPackage):
	"""Visualizations for 'mlr3'

	Visualization package of the 'mlr3' ecosystem. It features plots
    for mlr3 objects such as tasks, learners, predictions, benchmark results,
    tuning instances and filters via the 'autoplot()' generic of 'ggplot2'.
    The package draws plots with the 'viridis' color palette and applies the
    minimal theme. Visualizations include barplots, boxplots, histograms, ROC
    curves, and Precision-Recall curves.
	"""
	
	homepage = "https://mlr3viz.mlr-org.com"
	cran = "mlr3viz" 

	version("0.7.0", md5="71000fff902bf882d9b42709944ff328")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-mlr3misc@0.7:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
