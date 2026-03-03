# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtutable(RPackage):
	"""North Temperate Lakes - Microbial Observatory 16S Time Series
Data and Functions

	Analyses of OTU tables produced by 16S rRNA gene amplicon sequencing, as well as example data. It contains the data and scripts used in the paper Linz, et al. (2017) "Bacterial community composition and dynamics spanning five years in freshwater bog lakes," <doi: 10.1128/mSphere.00169-17>.
	"""
	
	cran = "OTUtable" 

	version("1.1.2", md5="d9ad45c5917ab88c30f5fb2c20bdb479")

	depends_on("r@2.10:", type=("build", "run"))
