# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscauc(RPackage):
	"""Linear and Non-Linear AUC for Discounting Data

	Area under the curve (AUC; Myerson et al., 2001) <doi:10.1901/jeab.2001.76-235> 
  is a popular measure used in discounting research. Although the calculation of
  AUC is standardized, there are differences in AUC based on some assumptions. 
  For example, Myerson et al. (2001) <doi:10.1901/jeab.2001.76-235> 
  assumed that (with delay discounting data) a researcher would impute an
  indifference point at zero delay equal to the value of the larger, later outcome.
  However, this practice is not clearly followed. This imputed zero-delay indifference
  point plays an important role in log and ordinal versions of AUC.
  Ordinal and log versions of AUC are described by Borges et al. (2016)<doi:10.1002/jeab.219>. 
  The package can calculate all three versions of AUC [and includes a new version: IHS(AUC)],
  impute indifference points when x = 0, calculate ordinal AUC in the case of Halton
  sampling of x-values, and account for probability discounting AUC.
	"""
	
	cran = "discAUC" 

	version("1.0.0", md5="0ba06f83bc55a474765996b2309acd37")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
