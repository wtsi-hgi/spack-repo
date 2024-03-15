# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusevol(RPackage):
	"""A Procedure for Cluster Evolution Analytics

	Cluster Evolution Analytics allows us to use exploratory what if questions in the sense that the present information of an object is plugged-in a dataset in a previous time frame so that we can explore its evolution (and of its neighbors) to the present. See the URL for the papers associated with this package, as for instance, Morales-Oñate and Morales-Oñate (2024) <https://mpra.ub.uni-muenchen.de/120220>.
	"""
	
	homepage = "https://github.com/vmoprojs/clusEvol"
	cran = "clusEvol" 

	version("1.0.0", md5="4a299724eb10b9701541705f7ca294e8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-clustersim", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
