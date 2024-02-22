# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrc(RPackage):
	"""Multi-Visit Closed Population Mark-Recapture Estimates

	Compute bootstrap confidence intervals for the adjusted Schnabel and Schumacher-Eschmeyer multi-visit mark-recapture estimators based on Dettloff (2023) <doi:10.1016/j.fishres.2023.106756>.
	"""
	
	homepage = "https://github.com/k-dettloff/mRc"
	cran = "mRc" 

	version("0.1.0", md5="f004397686c3ad7338a3e2020be0d3e2")

