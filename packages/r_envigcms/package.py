# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvigcms(RPackage):
	"""GC/LC-MS Data Analysis for Environmental Science

	Gas/Liquid Chromatography-Mass Spectrometer(GC/LC-MS) Data Analysis for Environmental Science. This package covered topics such molecular isotope ratio, matrix effects and Short-Chain Chlorinated Paraffins analysis etc. in environmental analysis.
	"""
	
	homepage = "https://github.com/yufree/enviGCMS"
	cran = "enviGCMS" 

	version("0.7.1", md5="d5097fc50c50ffb312a4865d2e281727")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdisop", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-animation@2.2.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
