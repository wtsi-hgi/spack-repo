# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfercsn(RPackage):
	"""Inferring Cell-Specific Gene Regulatory Network

	A method for inferring cell-specific gene regulatory network from single-cell sequencing data.
	"""
	
	homepage = "https://mengxu98.github.io/inferCSN/"
	cran = "inferCSN" 

	version("1.0.1", md5="68abfddc1d3eedb02a071e49c4a48054")
	version("1.0.0", md5="ca97beeae391b37f68f4a3ac5d6e4b64")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
