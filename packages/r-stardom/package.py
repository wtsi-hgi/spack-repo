# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStardom(RPackage):
	"""PARAFAC Analysis of EEMs from DOM

	This is a user-friendly way to run a parallel factor (PARAFAC) analysis (Harshman, 1971) <doi:10.1121/1.1977523> on excitation emission matrix (EEM) data from dissolved organic matter (DOM) samples (Murphy et al., 2013) <doi:10.1039/c3ay41160e>. The analysis includes profound methods for model validation. Some additional functions allow the calculation of absorbance slope parameters and create beautiful plots.
	"""
	
	homepage = "https://cran.r-project.org/package=staRdom"
	cran = "staRdom" 

	version("1.1.28", md5="99fb633a9271042a0427c66062594bbe")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-eemr@1.0.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-pracma@2.3.3:", type=("build", "run"))
	depends_on("r-zoo@1.8.12:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-multiway@1.0.6:", type=("build", "run"))
	depends_on("r-ggally@2.1.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.16:", type=("build", "run"))
	depends_on("r-drc@3.0.1:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-matrixstats@1:", type=("build", "run"))
	depends_on("r-mba@0.1.0:", type=("build", "run"))
	depends_on("r-cdom@0.1:", type=("build", "run"))
	depends_on("r-r-matlab@3.7:", type=("build", "run"))
	depends_on("r-readr@2.1.4:", type=("build", "run"))
	depends_on("r-gtools@3.9.4:", type=("build", "run"))
	depends_on("r-viridislite@0.4.2:", type=("build", "run"))
