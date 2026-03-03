# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpred(RPackage):
	"""Predictor Identifier: Nonparametric Prediction

	Partial informational correlation (PIC) is used to identify the meaningful predictors to the response from a large set of potential predictors. Details of methodologies used in the package can be found in Sharma, A., Mehrotra, R. (2014). <doi:10.1002/2013WR013845>, Sharma, A., Mehrotra, R., Li, J., & Jha, S. (2016). <doi:10.1016/j.envsoft.2016.05.021>, and Mehrotra, R., & Sharma, A. (2006). <doi:10.1016/j.advwatres.2005.08.007>.
	"""
	
	homepage = "https://github.com/zejiang-unsw/NPRED#readme"
	cran = "NPRED" 

	version("1.0.7", md5="8469b476c13f3db153457e31e4eaf21a")

	depends_on("r@3.4:", type=("build", "run"))
