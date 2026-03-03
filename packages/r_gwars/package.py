# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwars(RPackage):
	"""Manhattan, Q-Q, and PCA Plots using 'ggplot2'

	Generate Manhattan, Q-Q, and PCA plots from GWAS and PCA results using 'ggplot2'.
	"""
	
	homepage = "https://github.com/LindoNkambule/gwaRs"
	cran = "gwaRs" 

	version("0.3.0", md5="2f782e39f8f59e6e912332aec9b37547")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
