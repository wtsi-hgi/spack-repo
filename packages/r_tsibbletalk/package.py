# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsibbletalk(RPackage):
	"""Interactive Graphics for Tsibble Objects

	A shared tsibble data easily communicates between
    htmlwidgets on both client and server sides, powered by 'crosstalk'. A
    shiny module is provided to visually explore periodic/aperiodic
    temporal patterns.
	"""
	
	cran = "tsibbletalk" 

	version("0.1.0", md5="5e0e25d9b4138bd8668bb2e22bcb89b1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crosstalk@1.1.0.1:", type=("build", "run"))
	depends_on("r-dendextend@1.13.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-glue@1.4.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-plotly@4.9.2.1:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-tsibble@0.9.1:", type=("build", "run"))
	depends_on("r-vctrs@0.3.1:", type=("build", "run"))
