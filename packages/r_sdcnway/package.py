# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdcnway(RPackage):
	"""Tools to Evaluate Disclosure Risk

	Tools for calculating disclosure risk measures for microdata,
    including record-level and file-level measures. The record-level disclosure
    risk is estimated primarily using exhaustive tabulation. The file-level
    disclosure risk is estimated by fitting loglinear models on the observed 
    sample counts in cells formed by key variables and their interactions. 
    Funded by the National Center for Education Statistics. See Skinner and
    Shlomo (2008) <doi:10.1198/016214507000001328> for a description of the
    file-level risk measures and the loglinear model approach.
	"""
	
	cran = "SDCNway" 

	version("1.0.1", md5="0ffbc4c7ced245e2c65781736904212d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-plyr@1.8.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-mass@3.6:", type=("build", "run"))
