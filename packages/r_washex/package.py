# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWashex(RPackage):
	"""Washington State Legislative Explorer

	Gets data from the Washington State Legislature.
	"""
	
	homepage = "https://github.com/rwrandles/washex-r"
	cran = "washex" 

	version("1.2.0", md5="438671ea3b8353b08e6f109ad23c1ee9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xml@3.99.0.5:", type=("build", "run"))
