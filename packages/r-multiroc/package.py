# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiroc(RPackage):
	"""Calculating and Visualizing ROC and PR Curves Across Multi-Class
Classifications

	Tools to solve real-world problems with multiple classes classifications by computing the areas under ROC and PR curve via micro-averaging and macro-averaging. The vignettes of this package can be found via <https://github.com/WandeRum/multiROC>. The methodology is described in V. Van Asch (2013) <https://www.clips.uantwerpen.be/~vincent/pdf/microaverage.pdf> and Pedregosa et al. (2011) <http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html>.
	"""
	
	cran = "multiROC" 

	version("1.1.1", md5="eb54cf12f0690a738b34d222ea330731")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
