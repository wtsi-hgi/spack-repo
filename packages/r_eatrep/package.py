# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REatrep(RPackage):
	"""Educational Assessment Tools for Replication Methods

	Replication methods to compute some basic statistic operations (means, standard deviations,
  frequency tables, percentiles and generalized linear models) in complex survey designs comprising multiple
  imputed variables and/or a clustered sampling structure which both deserve special procedures at least in
  estimating standard errors. See the package documentation for a more detailed description along with references.
	"""
	
	homepage = "https://github.com/weirichs/eatRep"
	cran = "eatRep" 

	version("0.14.7", md5="3a52f2c0894c1688916665b911ac9f36")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-survey@4.1.1:", type=("build", "run"))
	depends_on("r-bifiesurvey", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-lavaan@0.6.7:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-mice@2.46:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-miceadds", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-effectliter", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-eattools@0.7.4:", type=("build", "run"))
	depends_on("r-eatgads@0.20:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
