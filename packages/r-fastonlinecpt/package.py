# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastonlinecpt(RPackage):
	"""Online Multivariate Changepoint Detection

	Implementation of a simple algorithm designed for online multivariate changepoint detection of a mean in sparse changepoint settings. The algorithm is based on a modified cusum statistic and guarantees control of the type I error on any false discoveries, while featuring O(1) time and O(1) memory updates per series as well as a proven detection delay.
	"""
	
	cran = "fastOnlineCpt" 

	version("1.0", md5="66d01e466c8af285bc24dde3b480db9b")

	depends_on("r-rdpack", type=("build", "run"))
