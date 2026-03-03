# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasketballanalyzer(RPackage):
	"""Analysis and Visualization of Basketball Data

	Contains data and code to accompany  the book 
             P. Zuccolotto and M. Manisera (2020) Basketball Data Science. Applications with R. CRC Press. ISBN 9781138600799.
	"""
	
	homepage = "https://github.com/sndmrc/BasketballAnalyzeR"
	cran = "BasketballAnalyzeR" 

	version("0.5.0", md5="314fad27fc8c9b333cbfcbe317dae67c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-hexbin@1.27:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-directlabels@2018.5:", type=("build", "run"))
	depends_on("r-corrplot@0.80:", type=("build", "run"))
	depends_on("r-ggplotify@0.0.3:", type=("build", "run"))
	depends_on("r-network@1.13:", type=("build", "run"))
	depends_on("r-sna@2.4:", type=("build", "run"))
	depends_on("r-dendextend@1.8:", type=("build", "run"))
	depends_on("r-circlize@0.4:", type=("build", "run"))
	depends_on("r-pbsmapping@2.70:", type=("build", "run"))
	depends_on("r-sp@1.3:", type=("build", "run"))
	depends_on("r-operators@0.1:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-ggally@1.4:", type=("build", "run"))
	depends_on("r-statnet-common@4.2:", type=("build", "run"))
	depends_on("r-ggnetwork@0.5:", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
