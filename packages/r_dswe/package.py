# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDswe(RPackage):
	"""Data Science for Wind Energy

	Data science methods used in wind energy applications. 
              Current functionalities include creating a multi-dimensional power curve model, 
              performing power curve function comparison, covariate matching, and energy decomposition. 
              Relevant works for the developed functions are: 
              funGP() - Prakash et al. (2022) <doi:10.1080/00401706.2021.1905073>, 
              AMK() - Lee et al. (2015) <doi:10.1080/01621459.2014.977385>, 
              tempGP() - Prakash et al. (2022) <doi:10.1080/00401706.2022.2069158>, 
              ComparePCurve() - Ding et al. (2021) <doi:10.1016/j.renene.2021.02.136>,
              deltaEnergy() - Latiffianti et al. (2022) <doi:10.1002/we.2722>,
              syncSize() - Latiffianti et al. (2022) <doi:10.1002/we.2722>,
              imptPower() - Latiffianti et al. (2022) <doi:10.1002/we.2722>,
              All other functions - Ding (2019, ISBN:9780429956508).
	"""
	
	homepage = "https://github.com/TAMU-AML/DSWE-Package"
	cran = "DSWE" 

	version("1.8.2", md5="357a5d7d2d12964122594639fb1d8412")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@1.0.4.6:", type=("build", "run"))
	depends_on("r-matrixstats@0.55:", type=("build", "run"))
	depends_on("r-fnn@1.1.3:", type=("build", "run"))
	depends_on("r-kernsmooth@2.23.16:", type=("build", "run"))
	depends_on("r-mixtools@1.1:", type=("build", "run"))
	depends_on("r-gss@2.2.2:", type=("build", "run"))
	depends_on("r-e1071@1.7.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-xgboost@1.7.7.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.870.2:", type=("build", "run"))
