# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCartograflow(RPackage):
	"""Filtering Matrix for Flow Mapping

	Functions to prepare and filter an origin-destination matrix for thematic flow mapping purposes.   
             This comes after Bahoken, Francoise (2016), Mapping flow matrix a contribution, PhD in Geography - Territorial sciences. See Bahoken (2017) <doi:10.4000/netcom.2565>.
	"""
	
	homepage = "https://github.com/fbahoken/cartogRaflow"
	cran = "cartograflow" 

	version("1.0.5", md5="da677e32ca1241944ba585ad8223efbd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
