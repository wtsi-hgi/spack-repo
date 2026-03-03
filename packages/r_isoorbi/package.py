# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoorbi(RPackage):
	"""Process Orbitrap Isotopocule Data

	Read and process isotopocule data from an Orbitrap Isotope Solutions mass spectrometer. Citation: Kantnerova et al. (in review).
	"""
	
	homepage = "https://github.com/isoverse/isoorbi"
	cran = "isoorbi" 

	version("1.3.0", md5="18a55d889a3cc9914e4320dee57d8b08")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
