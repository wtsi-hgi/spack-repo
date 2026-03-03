# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMctq(RPackage):
	"""Tools to Process the Munich ChronoType Questionnaire (MCTQ)

	A complete toolkit to process the Munich ChronoType 
    Questionnaire (MCTQ) for its three versions (standard, micro, and shift). 
    MCTQ is a quantitative and validated tool to assess chronotypes using 
    peoples' sleep behavior, originally presented by Till Roenneberg, Anna 
    Wirz-Justice, and Martha Merrow (2003, <doi:10.1177/0748730402239679>).
	"""
	
	homepage = "https://docs.ropensci.org/mctq/"
	cran = "mctq" 

	version("0.3.2", md5="38a40a15c59b83a98f74c53869d25b89")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-hms@1.1.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
