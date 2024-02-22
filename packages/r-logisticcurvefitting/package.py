# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogisticcurvefitting(RPackage):
	"""Logistic Curve Fitting by Rhodes Method

	A system for fitting Logistic Curve by Rhodes Method. Method for fitting logistic curve by Rhodes Method is described in A.M.Gun,M.K.Gupta and B.Dasgupta(2019,ISBN:81-87567-81-3).
	"""
	
	cran = "LogisticCurveFitting" 

	version("0.1.0", md5="46d6ca856bc70a1d7b0572021c2a1561")

