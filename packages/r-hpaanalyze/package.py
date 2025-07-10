# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpaanalyze(RPackage):
	"""Retrieve and analyze data from the Human Protein Atlas

	Provide functions for retrieving, exploratory analyzing and visualizing the Human Protein Atlas data.
	"""
	
	homepage = "https://github.com/anhtr/HPAanalyze"
	bioc = "HPAanalyze" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HPAanalyze_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HPAanalyze/HPAanalyze_1.20.0.tar.gz"]

	version("1.20.0", sha256="1f36584e878c2fc704d4e143df33e38061b3c2a5073eef4eb5db51b774b254f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
