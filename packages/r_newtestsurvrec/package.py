# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewtestsurvrec(RPackage):
	"""Statistical Tests to Compare Curves with Recurrent Events

	Implements the routines to compare the survival curves with recurrent events, including the estimations of survival curves. The first model is a  model for recurrent event, when the data are correlated or not  correlated. It was proposed by Wang and Chang (1999) <doi:10.2307/2669690>. In the independent case, the survival function can be  estimated by the generalization of the limit product model of Pena (2001) <doi:10.1198/016214501753381922>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "newTestSurvRec" 

	version("1.0.2", md5="d8bb332aae02a45d3a77cf959313af12")

	depends_on("r@3.4:", type=("build", "run"))
