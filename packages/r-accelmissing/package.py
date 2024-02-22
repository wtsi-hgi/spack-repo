# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccelmissing(RPackage):
	"""Missing Value Imputation for Accelerometer Data

	Imputation for the missing count values in accelerometer data. The methodology includes both parametric and semi-parametric multiple imputations under the zero-inflated Poisson lognormal model. This package also provides multiple functions to pre-process the accelerometer data previous to the missing data imputation. These includes detecting wearing and non-wearing time, selecting valid days and subjects, and creating plots.
	"""
	
	cran = "accelmissing" 

	version("1.4", md5="4c93ab135bd717c9c0c5e7dadac6a099")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
