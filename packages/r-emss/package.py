# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmss(RPackage):
	"""Some EM-Type Estimation Methods for the Heckman Selection Model

	Some EM-type algorithms to estimate parameters for the well-known Heckman selection model are provided in the package. Such algorithms are as follow: ECM(Expectation/Conditional Maximization), ECM(NR)(the Newton-Raphson method is adapted to the ECM) and ECME(Expectation/Conditional Maximization Either). Since the algorithms are based on the EM algorithm, they also have EM’s main advantages, namely, stability and ease of implementation. Further details and explanations of the algorithms can be found in Zhao et al. (2020) <doi: 10.1016/j.csda.2020.106930>.
	"""
	
	homepage = "https://github.com/SangkyuStat/EMSS"
	cran = "EMSS" 

	version("1.1.1", md5="27749be659945d26a5e870dc49f87ccd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sampleselection", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
