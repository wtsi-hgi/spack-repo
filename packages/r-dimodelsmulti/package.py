# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimodelsmulti(RPackage):
	"""Fit Multivariate Diversity-Interactions Models with Repeated
Measures

	An add-on package to 'DImodels' for the fitting of biodiversity and ecosystem function relationship study data with multiple ecosystem function responses and/or time points. This package uses the multivariate and repeated measures Diversity-Interactions (DI) methods developed by Kirwan et al. (2009) <doi:10.1890/08-1684.1>, Finn et al. (2013) <doi:10.1111/1365-2664.12041>, and Dooley et al. (2015) <doi:10.1111/ele.12504>.
	"""
	
	homepage = "https://dimodels.com"
	cran = "DImodelsMulti" 

	version("1.0.1", md5="5d23618e548f06cf3bda0259a528e4b9")
	version("1.0", md5="fc1cccb928b0e2cdbfcedd1eeeda518c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dimodels", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
