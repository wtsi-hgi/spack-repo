# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomforestexplainer(RPackage):
	"""Explaining and Visualizing Random Forests in Terms of Variable
Importance

	A set of tools to help explain which variables are most important in a random forests. Various variable importance measures are calculated and visualized in different settings in order to get an idea on how their importance changes depending on our criteria (Hemant Ishwaran and Udaya B. Kogalur and Eiran Z. Gorodeski and Andy J. Minn and Michael S. Lauer (2010) <doi:10.1198/jasa.2009.tm08622>, Leo Breiman (2001) <doi:10.1023/A:1010933404324>).
	"""
	
	homepage = "https://github.com/ModelOriented/randomForestExplainer"
	cran = "randomForestExplainer" 

	version("0.10.1", md5="a51387293f8478091b20e58fd5cf0684")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.1:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-ggally@1.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.6.5:", type=("build", "run"))
	depends_on("r-randomforest@4.6.12:", type=("build", "run"))
	depends_on("r-ranger@0.9:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-rmarkdown@1.5:", type=("build", "run"))
