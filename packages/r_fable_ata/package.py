# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFableAta(RPackage):
	"""'ATAforecasting' Modelling Interface for 'fable' Framework

	Allows ATA (Automatic Time series analysis using the Ata method) models from the 'ATAforecasting' package to be used in a tidy workflow with the modeling interface of
    'fabletools'. This extends 'ATAforecasting' to provide enhanced model specification and management, performance evaluation methods, and
    model combination tools. The Ata method (Yapar et al. (2019) <doi:10.15672/hujms.461032>), an alternative to exponential smoothing (described in Yapar (2016)
    <doi:10.15672/HJMS.201614320580>, Yapar et al. (2017) <doi:10.15672/HJMS.2017.493>), is a new univariate time series forecasting method which provides
    innovative solutions to issues faced during the initialization and optimization stages of existing forecasting methods.
    Forecasting performance of the Ata method is superior to existing methods both in terms of easy implementation and accurate forecasting.
    It can be applied to non-seasonal or seasonal time series which can be decomposed into four components (remainder, level, trend and seasonal).
	"""
	
	homepage = "https://alsabtay.github.io/fable.ata/"
	cran = "fable.ata" 

	version("0.0.6", md5="1c6dcdc6b39b892653f36fd7b8fb522c")

	depends_on("r-fabletools@0.3.3:", type=("build", "run"))
	depends_on("r-ataforecasting@0.0.60:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-distributional", type=("build", "run"))
	depends_on("r-tsbox", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
