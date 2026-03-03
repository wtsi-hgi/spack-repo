# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWcde(RPackage):
	"""Download Data from the Wittgenstein Centre Human Capital Data
Explorer

	Download and plot education specific demographic data from the Wittgenstein Centre for Demography and Human Capital Data Explorer <http://dataexplorer.wittgensteincentre.org/>.
	"""
	
	homepage = "https://guyabel.github.io/wcde/"
	cran = "wcde" 

	version("0.0.7", md5="54c37cfa801667f121eb68298834f325")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
