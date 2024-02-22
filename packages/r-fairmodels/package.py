# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFairmodels(RPackage):
	"""Flexible Tool for Bias Detection, Visualization, and Mitigation

	Measure fairness metrics in one place for many models. Check how big is model's bias towards different races, sex, nationalities etc. Use measures such as Statistical Parity, Equal odds to detect the discrimination against unprivileged groups. Visualize the bias using heatmap, radar plot, biplot, bar chart (and more!). There are various pre-processing and post-processing bias mitigation algorithms implemented. Package also supports calculating fairness metrics for regression models. Find more details in (Wiśniewski, Biecek (2021)) <arXiv:2104.00507>.  
	"""
	
	homepage = "https://fairmodels.drwhy.ai/"
	cran = "fairmodels" 

	version("1.2.1", md5="e843a9613fd6348bc2698b43dc6689ab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
