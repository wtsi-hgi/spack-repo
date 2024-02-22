# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgeoPlot(RPackage):
	"""Plot ForestGEO Data

	To help you access, transform, analyze, and visualize
    ForestGEO data, we developed a collection of R packages
    (<https://forestgeo.github.io/fgeo/>). This package, in particular,
    helps you to plot ForestGEO data. To learn more about ForestGEO visit
    <https://forestgeo.si.edu/>.
	"""
	
	homepage = "https://github.com/forestgeo/fgeo.plot"
	cran = "fgeo.plot" 

	version("1.1.11", md5="6febfe6e7db278dd7b155e0377636493")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-fgeo-tool@1.2.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.8.1:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
