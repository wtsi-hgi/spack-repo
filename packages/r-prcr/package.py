# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrcr(RPackage):
	"""Person-Centered Analysis

	Provides an easy-to-use yet adaptable set of tools to conduct person-center analysis using a two-step clustering procedure. As described in Bergman and El-Khouri (1999) <DOI:10.1002/(SICI)1521-4036(199910)41:6%3C753::AID-BIMJ753%3E3.0.CO;2-K>, hierarchical clustering is performed to determine the initial partition for the subsequent k-means clustering procedure.
	"""
	
	homepage = "https://github.com/jrosen48/prcr"
	cran = "prcr" 

	version("0.2.1", md5="5220a6c468e1111c73fc88db615c0d34")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
