# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROverviewr(RPackage):
	"""Easily Extracting Information About Your Data

	Makes it easy to display descriptive information on a data
    set.  Getting an easy overview of a data set by displaying and
    visualizing sample information in different tables (e.g., time and
    scope conditions).  The package also provides publishable 'LaTeX' code
    to present the sample information.
	"""
	
	homepage = "https://github.com/cosimameyer/overviewR"
	cran = "overviewR" 

	version("0.0.13", md5="eebcc573dd7279ce9e218608af4ef998")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-ggrepel@0.8.2:", type=("build", "run"))
	depends_on("r-ggvenn@0.1.8:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
