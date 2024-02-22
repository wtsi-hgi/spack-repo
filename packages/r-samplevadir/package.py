# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplevadir(RPackage):
	"""Draw Stratified Samples from the VADIR Database

	Affords researchers the ability to draw stratified samples from the U.S. Department of Veteran's Affairs/Department of Defense Identity Repository (VADIR) database according to a variety of population characteristics. The VADIR database contains information for all veterans who were separated from the military after 1980. The central utility of the present package is to integrate data cleaning and formatting for the VADIR database with the stratification methods described by Mahto (2019) <https://CRAN.R-project.org/package=splitstackshape>. Data from VADIR are not provided as part of this package.
	"""
	
	homepage = "https://github.com/tswanson222/sampleVADIR"
	cran = "sampleVADIR" 

	version("1.0.0", md5="528a07be1c35d636de252499570ad2a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
