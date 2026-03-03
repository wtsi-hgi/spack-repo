# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgenmpp(RPackage):
	"""QTL Mapping for Multi Parent Populations

	For Multi Parent Populations (MPP) Identity By Descend (IBD) 
    probabilities are computed using Hidden Markov Models. These probabilities 
    are then used in a mixed model approach for QTL Mapping as described in 
    Li et al. (<doi:10.1007/s00122-021-03919-7>).
	"""
	
	cran = "statgenMPP" 

	version("1.0.2", md5="a0c3483f17bc74e968e0ccbc7a7b1e9f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-statgengwas@1.0.8:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lmmsolver", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-statgenibd@1.0.4:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
