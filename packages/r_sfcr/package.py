# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfcr(RPackage):
	"""Simulate Stock-Flow Consistent Models

	Routines to write, simulate, and validate stock-flow consistent (SFC) models. The accounting structure of SFC models are described in Godley and Lavoie (2007, ISBN:978-1-137-08599-3). The algorithms implemented to solve the models (Gauss-Seidel and Broyden) are described in Kinsella and O'Shea (2010) <doi:10.2139/ssrn.1729205> and Peressini and Sullivan (1988, ISBN:0-387-96614-5).
	"""
	
	homepage = "https://github.com/joaomacalos/sfcr"
	cran = "sfcr" 

	version("0.2.1", md5="6fbccba7d4af4baba68714ebad1ab1b0")

	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-expm@0.999.5:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-igraph@1.2.6:", type=("build", "run"))
	depends_on("r-kableextra@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rdpack@2.1:", type=("build", "run"))
	depends_on("r-rootsolve@1.8.2.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-vctrs@0.3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
