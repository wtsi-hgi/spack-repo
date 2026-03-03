# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpbkg(RPackage):
	"""Detecting New Signals under Background Mismodelling

	Given a postulated model and a set of data, the comparison density is estimated and the deviance test is implemented in order to assess if the data distribution deviates significantly from the postulated model. Finally, the results are summarized in a CD-plot as described in Algeri S. (2019) <arXiv:1906.06615>. 
	"""
	
	cran = "LPBkg" 

	version("1.2", md5="17895540076b1157c2283ac0b15307f8")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
