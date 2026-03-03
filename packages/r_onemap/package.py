# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnemap(RPackage):
	"""Construction of Genetic Maps in Experimental Crosses

	Analysis of molecular marker data from model (backcrosses,
    F2 and recombinant inbred lines) and non-model systems (i. e.
    outcrossing species). For the later, it allows statistical
    analysis by simultaneously estimating linkage and linkage
    phases (genetic map construction) according to Wu et al. (2002)
    <doi:10.1006/tpbi.2002.1577>. All analysis are based on multipoint 
    approaches using hidden Markov models.
	"""
	
	homepage = "https://github.com/augusto-garcia/onemap"
	cran = "onemap" 

	version("3.0.0", md5="220a74a0720e4f5e89550a3162167d32")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-plotly@4.7.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-rcpp@0.10.5:", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-rebus", type=("build", "run"))
	depends_on("r-vcfr@1.6:", type=("build", "run"))
