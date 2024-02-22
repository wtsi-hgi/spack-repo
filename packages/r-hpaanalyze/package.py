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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HPAanalyze_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HPAanalyze/HPAanalyze_1.20.0.tar.gz"]

	version("1.20.0", md5="0916d6c86a23a3c136b3d0f1de2a25f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
