# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTetraclasse(RPackage):
	"""Satisfaction Analysis using Tetraclasse Model and Llosa Matrix

	The satisfaction Analysis using the tetraclasse model from Sylvie Llosa. Llosa (1997) <http://www.jstor.org/stable/40592578>.
	"""
	
	cran = "tetraclasse" 

	version("0.1.21", md5="c7204c944bd27d75cd324564588749ae")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
