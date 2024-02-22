# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhit(RPackage):
	"""OGA+HDIC+Trim and High-Dimensional Linear Regression Models

	Ing and Lai (2011) <doi:10.5705/ss.2010.081> proposed a high-dimensional model selection procedure that comprises three steps: orthogonal greedy algorithm (OGA), high-dimensional information criterion (HDIC), and Trim. The first two steps, OGA and HDIC, are used to sequentially select input variables and determine stopping rules, respectively. The third step, Trim, is used to delete irrelevant variables remaining in the second step. This package aims at fitting a high-dimensional linear regression model via OGA+HDIC+Trim.
	"""
	
	homepage = "http://mx.nthu.edu.tw/~cking/pdf/IngLai2011.pdf"
	cran = "Ohit" 

	version("1.0.0", md5="a5fd882784cf2dfe96879f86ae3fafe5")

