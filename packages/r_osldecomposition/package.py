# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsldecomposition(RPackage):
	"""Signal Component Analysis for Optically Stimulated Luminescence

	Function library for the identification and separation of exponentially
    decaying signal components in continuous-wave optically stimulated luminescence measurements.
    A special emphasis is laid on luminescence dating with quartz, which is known for
    systematic errors due to signal components with unequal physical behaviour.
    Also, this package enables an easy to use signal decomposition of
    data sets imported and analysed with the R package 'Luminescence'.
    This includes the optional automatic creation of HTML reports. Further information and tutorials
    can be found at <https://luminescence.de>.
	"""
	
	cran = "OSLdecomposition" 

	version("1.0.0", md5="d8bae9dc6482e3b781c37c09443fe258")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-luminescence@0.9.9:", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
