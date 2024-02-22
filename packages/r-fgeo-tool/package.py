# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgeoTool(RPackage):
	"""Import and Manipulate 'ForestGEO' Data

	To help you access, transform, analyze, and visualize
    'ForestGEO' data, we developed a collection of R packages
    (<https://forestgeo.github.io/fgeo/>). This package, in particular,
    helps you to easily import, filter, and modify 'ForestGEO' data. To
    learn more about 'ForestGEO' visit <https://forestgeo.si.edu/>.
	"""
	
	homepage = "https://forestgeo.github.io/fgeo.tool/"
	cran = "fgeo.tool" 

	version("1.2.9", md5="1e585cb939d865a2f403f192d02a1d54")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-tidyselect@0.2.5:", type=("build", "run"))
