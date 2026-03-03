# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWgteff(RPackage):
	"""Functions for Weighting Effects

	Functions for determining the effect of data weights on the variance of survey data: users will load a data set which has a weights column, and the package will calculate the design effect (DEFF), weighting loss, root design effect (DEFT), effective sample size (ESS), and/or weighted margin of error.
	"""
	
	cran = "WgtEff" 

	version("0.1.2", md5="931cbff245796883f447b31a57a145da")

	depends_on("r@3.5:", type=("build", "run"))
