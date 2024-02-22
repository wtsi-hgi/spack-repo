# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIzid(RPackage):
	"""Identify Zero-Inflated Distributions

	Computes bootstrapped Monte Carlo estimate of p value of Kolmogorov-Smirnov (KS) test and 
    likelihood ratio test for zero-inflated count data, based on the work of Aldirawi et al. (2019) 
    <doi:10.1109/BHI.2019.8834661>. With the package, user can also find tools to simulate 
    random deviates from zero inflated or hurdle models and obtain  maximum likelihood estimate
    of unknown parameters in these models.
	"""
	
	cran = "iZID" 

	version("0.0.1", md5="a53e7738de6b2c7222e68b00a140b9a0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-extradistr@1.8.11:", type=("build", "run"))
	depends_on("r-rootsolve@1.7:", type=("build", "run"))
	depends_on("r-foreach@1.4.7:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
