# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlovan(RPackage):
	"""Geostatistics Methods and Klovan Data

	A comprehensive set of geostatistical, visual,
    and analytical methods, in conjunction with the expanded version of the
    acclaimed J.E. Klovan's mining dataset, are included in 'klovan'. This makes the
    package an excellent learning resource for Principal Component Analysis (PCA),
    Factor Analysis (FA), kriging, and other geostatistical techniques. Originally
    published in the 1976 book 'Geological Factor Analysis', the included mining
    dataset was assembled by Professor J. E. Klovan of the University of Calgary.
    Being one of the first applications of FA in the geosciences, this dataset has
    significant historical importance. As a well-regarded and published dataset, it
    is an excellent resource for demonstrating the capabilities of PCA, FA, kriging,
    and other geostatistical techniques in geosciences. For those interested in
    these methods, the 'klovan' datasets provide a valuable and illustrative resource.
    Note that some methods require the 'RGeostats' package. Please refer to the
    README or Additional_repositories for installation instructions. This material is
    based upon research in the Materials Data Science for Stockpile Stewardship Center
    of Excellence (MDS3-COE), and supported by the Department of Energy's National
    Nuclear Security Administration under Award Number DE-NA0004104.
	"""
	
	cran = "klovan" 

	version("0.1.0", md5="9f27afcb9fdae5e68ccefadb25340244")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
