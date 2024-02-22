# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiscic(RPackage):
	"""Misclassified Interval Censored Time-to-Event Data

	Estimation of the survivor function for interval censored time-to-event data subject to misclassification using nonparametric maximum likelihood estimation, implementing the methods of Titman (2017) <doi:10.1007/s11222-016-9705-7>. Misclassification probabilities can either be specified as fixed or estimated. Models with time dependent misclassification may also be fitted. 
	"""
	
	cran = "miscIC" 

	version("0.1.0", md5="82fd3659ca1359d84535acddc543d550")

	depends_on("r-nnls", type=("build", "run"))
