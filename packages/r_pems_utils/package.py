# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPemsUtils(RPackage):
	"""Portable Emissions (and Other Mobile) Measurement System
Utilities

	Utility functions for the handling, analysis and visualisation 
    of data from portable emissions measurement systems ('PEMS') and other 
    similar mobile activity monitoring devices. The package includes a dedicated 
    'pems' data class that manages many of the quality control, unit handling 
    and data archiving issues that can hinder efforts to standardise 'PEMS' 
    research.
	"""
	
	homepage = "http://pems.r-forge.r-project.org/"
	cran = "pems.utils" 

	version("0.2.29.1", md5="c57e1cc51bf2b21855a8963b07b6bdbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-loa", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-baseline", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
