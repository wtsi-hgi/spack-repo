# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnestep(RPackage):
	"""One-Step Estimation

	Provide principally an eponymic function that numerically computes 
  the Le Cam's one-step estimator for an independent and identically distributed sample. 
  One-step estimation is asymptotically 
  efficient (see L. Le Cam (1956) <https://projecteuclid.org/euclid.bsmsp/1200501652>) 
  and can be computed faster than the maximum likelihood estimator for large observation 
  samples, see e.g. Brouste et al. (2021) <doi:10.32614/RJ-2021-044>.
	"""
	
	homepage = "https://journal.r-project.org/archive/2021/RJ-2021-044/"
	cran = "OneStep" 

	version("0.9.3", md5="58acad1ba5b93b886d7cde3df82c78cc")

	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
