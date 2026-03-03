# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REoa3(RPackage):
	"""Wildlife Mortality Estimator for Low Fatality Rates and
Imperfect Detection

	Evidence of Absence software (EoA) is a user-friendly application for estimating bird and bat fatalities at wind farms and designing search protocols. The software is particularly useful in addressing whether the number of fatalities has exceeded a given threshold and what search parameters are needed to give assurance that thresholds were not exceeded. The models are applicable even when zero carcasses have been found in searches, following Huso et al. (2015) <doi:10.1890/14-0764.1>, Dalthorp et al. (2017) <doi:10.3133/ds1055>, and Dalthorp and Huso (2015) <doi:10.3133/ofr20151227>.
	"""
	
	cran = "eoa3" 

	version("1.0.0.1", md5="232f059a5df39b06623566f80096d93f", url="https://cran.r-project.org/src/contrib/eoa3_1.0.0.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-genest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
