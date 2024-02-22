# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisreport(RPackage):
	"""Statistical Analysis of Misreporting on Sensitive Survey
Questions

	Enables investigation of the predictors of misreporting on sensitive survey questions through a multivariate list experiment regression method. The method permits researchers to model whether a survey respondent's answer to the sensitive item in a list experiment is different from his or her answer to an analogous direct question.
	"""
	
	cran = "misreport" 

	version("0.1.1", md5="dcf33beca8d8421f2b06e863967f6fa6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-numderiv@2014.2.1:", type=("build", "run"))
	depends_on("r-vgam@1.0.2:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.5:", type=("build", "run"))
