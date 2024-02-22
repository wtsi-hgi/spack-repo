# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdapoifd(RPackage):
	"""Partially Observed Integrated Functional Depth

	Applications to visualization, outlier detection and classification. Software companion for Elías, Antonio, Jiménez, Raúl, Paganoni, Anna M. and Sangalli, Laura M., (2022), "Integrated Depth for Partially Observed Functional Data". Journal of Computational and Graphical Statistics. <doi:10.1080/10618600.2022.2070171>.
	"""
	
	homepage = "https://github.com/aefdz/fdaPOIFD"
	cran = "fdaPOIFD" 

	version("1.0.3", md5="1ef945c00fd09c9161bdd43548457c6c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-fastgp", type=("build", "run"))
