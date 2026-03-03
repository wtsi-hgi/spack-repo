# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThrec(RPackage):
	"""Tree Height Response Calibration for Swedish Forests

	A tool that allows users to estimate tree height in the long-term forest experiments in Sweden. It utilizes the multilevel nonlinear mixed-effect height models developed for the forest experiments and consists of four functions for the main species, other conifer species, and other broadleaves. Each function within the system returns a data frame that includes the input data and the estimated heights for any missing values. Ogana et al. (2023) <doi:10.1016/j.foreco.2023.120843>n Arias-Rodil et al. (2015) <doi:10.1371/JOURNAL.PONE.0143521>.
	"""
	
	cran = "THREC" 

	version("1.0.0", md5="37aa71f7a8a383aa1722fbcc78336e9a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-deriv@1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
