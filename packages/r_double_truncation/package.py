# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoubleTruncation(RPackage):
	"""Analysis of Doubly-Truncated Data

	Likelihood-based inference methods with doubly-truncated data are developed under various models.
 Nonparametric models are based on Efron and Petrosian (1999) <doi:10.1080/01621459.1999.10474187> and
 Emura, Konno, and Michimae (2015) <doi:10.1007/s10985-014-9297-5>.
 Parametric models from the special exponential family (SEF) are based on
 Hu and Emura (2015) <doi:10.1007/s00180-015-0564-z> and
 Emura, Hu and Konno (2017) <doi:10.1007/s00362-015-0730-y>.
 The parametric location-scale models are based on Dorre et al. (2020) <doi:10.1007/s00180-020-01027-6>.
	"""
	
	cran = "double.truncation" 

	version("1.7", md5="008ca39668b949c3ff311c623ef01c0a")

