# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynthesis(RPackage):
	"""Generate Synthetic Data from Statistical Models

	Generate synthetic time series from commonly used statistical models, including linear, nonlinear and chaotic systems. Applications to testing methods can be found in Jiang, Z., Sharma, A., & Johnson, F. (2019) <doi:10.1016/j.advwatres.2019.103430> and Jiang, Z., Sharma, A., & Johnson, F. (2020) <doi:10.1029/2019WR026962> associated with an open-source tool by Jiang, Z., Rashid, M. M., Johnson, F., & Sharma, A. (2020) <doi:10.1016/j.envsoft.2020.104907>.
	"""
	
	homepage = "https://github.com/zejiang-unsw/synthesis#readme"
	cran = "synthesis" 

	version("1.2.4", md5="ad83ed0b2e35eb8c161bde3c904d021f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
