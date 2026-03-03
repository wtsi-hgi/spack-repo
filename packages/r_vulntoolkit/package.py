# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVulntoolkit(RPackage):
	"""Analysis of Tidal Datasets

	Contains functions for analysis and summary of tidal datasets. Also provides access to tidal data collected by the National Oceanic and Atmospheric Administration's Center for Operational Oceanographic Products and Services and the Permanent Service for Mean Sea Level. For detailed description and application examples, see Hill, T.D. and S.C. Anisfeld (2021) <doi:10.6084/m9.figshare.14161202.v1> and Hill, T.D. and S.C. Anisfeld (2015) <doi:10.1016/j.ecss.2015.06.004>.
	"""
	
	homepage = "https://github.com/troyhill/VulnToolkit"
	cran = "VulnToolkit" 

	version("1.1.4", md5="fa80a2031fd52f24c85c145374db084a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
