# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiingo(RPackage):
	"""An R Interface to the 'Tiingo' Stock Price API

	Functionality to download stock prices,
    cryptocurrency data, and more from the 'Tiingo' API
    <https://api.tiingo.com/>.
	"""
	
	homepage = "https://github.com/business-science/riingo"
	cran = "riingo" 

	version("0.3.1", md5="bd8714129fe8c26c347131d3a0fa2bfa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
