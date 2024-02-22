# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbfit(RPackage):
	"""A Double Bootstrap Method for Analyzing Linear Models with
Autoregressive Errors

	Computes the double bootstrap as discussed in McKnight, McKean, and Huitema (2000) <doi:10.1037/1082-989X.5.1.87>. 
              The double bootstrap method provides a better fit for a linear model with autoregressive errors than ARIMA when the sample size is small.
	"""
	
	cran = "DBfit" 

	version("2.0", md5="da196ed12c4ce3274ca5be1b84151564")

	depends_on("r-rfit", type=("build", "run"))
