# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZerotradeflow(RPackage):
	"""An Implementation for the Gravitational Models of Trade

	A system for creating the bilateral trade flow between a country
    pair equal to zero. You provide the data, tell get_zerotradeflow() which 
    variables are of interest and it expands the base by creating the bilateral
    zero trade flow. The bases on the flow of trade between countries only report
    positive trade (greater than zero), however, for some analyzes of gravitacional
    models, data on zero flow is also necessary. Some examples for Gravity Model:
    Figueiredo and Loures (2016) <doi:10.5935/0034-7140.20160015> and
    Yotov, Piermartini, Monteiro and Larch <https://vi.unctad.org/tpa/web/docs/vol2/book.pdf>.
	"""
	
	homepage = "https://github.com/AlexandreLoures/zerotradeflow"
	cran = "zerotradeflow" 

	version("0.1.0", md5="764e79cef31b4950d25da4894b1c40be")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
