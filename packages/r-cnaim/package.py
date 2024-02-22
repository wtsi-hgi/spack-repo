# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnaim(RPackage):
	"""Common Network Asset Indices Methodology (CNAIM)

	Implementation of the CNAIM standard in R. Contains a series of
    algorithms which determine the probability of failure, consequences of
    failure and monetary risk associated with electricity distribution
    companies' assets such as transformers and cables. Results are visualized
    in an easy-to-understand risk matrix.
	"""
	
	homepage = "https://www.cnaim.io/"
	cran = "CNAIM" 

	version("2.1.4", md5="4a23cdfce6d7d9a77b45b51a67b27015")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r2d3", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
