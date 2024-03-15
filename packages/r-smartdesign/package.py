# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartdesign(RPackage):
	"""Sequential Multiple Assignment Randomized Trial Design

	SMART trial design, as described by He, J., McClish, D., Sabo, R. (2021)  <doi:10.1080/19466315.2021.1883472>, includes multiple stages of randomization, where participants are randomized to an initial treatment in the first stage and then subsequently re-randomized between treatments in the following stage.
	"""
	
	homepage = "https://cran.r-project.org/package=smartDesign"
	cran = "smartDesign" 

	version("0.74", md5="028efa911166ec0379a89d1ea6ba9993")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
