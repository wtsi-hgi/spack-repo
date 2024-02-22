# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxanorm(RPackage):
	"""Feature-Wise Normalization for Microbiome Sequencing Data

	A novel feature-wise normalization method based on a zero-inflated negative binomial model. This method assumes that the effects of sequencing depth vary for each taxon on their mean and also incorporates a rational link of zero probability and taxon dispersion as a function of sequencing depth. Ziyue Wang, Dillon Lloyd, Shanshan Zhao, Alison Motsinger-Reif (2023) <doi:10.1101/2023.10.31.563648>.
	"""
	
	homepage = "https://github.com/wangziyue57/TaxaNorm"
	cran = "TaxaNorm" 

	version("2.4", md5="57bc5474b88c63982eed17e9e82f5d2e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-microbiome", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
