# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFingerpro(RPackage):
	"""Sediment Source Fingerprinting

	Quantifies the provenance of the sediments in a catchment or study area. Based on a comprehensive characterization of the sediment sources and the end sediment mixtures a mixing model algorithm is applied to the sediment mixtures in order to estimate the relative contribution of each potential source. The package includes several statistical methods such as Kruskal-Wallis test, discriminant function analysis ('DFA'), principal component plot ('PCA') to select the optimal subset of tracer properties. The variability within each sediment source is also considered to estimate the statistical distribution of the sources contribution.
	"""
	
	homepage = "https://github.com/eead-csic-eesa"
	cran = "fingerPro" 

	version("1.1", md5="0b46d5363e5204ec00697aa9cb2a502a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-klar@0.6.12:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ggally@1.3.2:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-rcmdr@2.4.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-reshape@0.8.7:", type=("build", "run"))
	depends_on("r-rgl@0.99.9:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-scales@0.5:", type=("build", "run"))
	depends_on("r-car@3:", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
