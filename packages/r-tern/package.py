# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTern(RPackage):
	"""Create Common TLGs Used in Clinical Trials

	Table, Listings, and Graphs (TLG) library for common outputs
    used in clinical trials.
	"""
	
	homepage = "https://github.com/insightsengineering/tern"
	cran = "tern" 

	version("0.9.3", md5="6e17cecf8c70a82f5d0520601cbcfcd8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rtables@0.6.6:", type=("build", "run"))
	depends_on("r-broom@0.5.4:", type=("build", "run"))
	depends_on("r-car@3.0.13:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-cowplot@0.7:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-emmeans@1.8:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-formatters@0.5.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-gtable@0.3:", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-survival@3.2.13:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
