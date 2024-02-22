# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeutralitytestr(RPackage):
	"""Test for a Neutral Evolutionary Model in Cancer Sequencing Data

	Package takes frequencies of mutations as reported by high throughput sequencing data from cancer and fits a theoretical neutral model of tumour evolution. Package outputs summary statistics and contains code for plotting the data and model fits. See Williams et al 2016 <doi:10.1038/ng.3489> and Williams et al 2017 <doi:10.1101/096305> for further details of the method.
	"""
	
	homepage = "https://github.com/marcjwilliams1/neutralitytestr"
	cran = "neutralitytestr" 

	version("0.0.3", md5="7083a3f7265a1eecb2e072ff226d5439")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
