# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTesiprov(RPackage):
	"""Calculation of Reliability and Failure Probability in Civil
Engineering

	Calculate the failure probability of civil engineering problems with Level I up to Level III Methods. Have fun and enjoy. References: Spaethe (1991, ISBN:3-211-82348-4) "Die Sicherheit tragender Baukonstruktionen", AU,BECK (2001) "Estimation of small failure probabilities in high dimensions by subset simulation." <doi:10.1016/S0266-8920(01)00019-4>, Breitung (1989) "Asymptotic approximations for probability integrals." <doi:10.1016/0266-8920(89)90024-6>.
	"""
	
	homepage = "https://www.hochschule-biberach.de/transfer/forschung/institut-fuer-konstruktiven-ingenieurbau"
	cran = "TesiproV" 

	version("0.9.2", md5="17e825263a018d963e56e8d2c9b615ef")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-edfun", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
