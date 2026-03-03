# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClam(RPackage):
	"""Classical Age-Depth Modelling of Cores from Deposits

	Performs 'classical' age-depth modelling of dated sediment deposits - prior to applying more sophisticated techniques such as Bayesian age-depth modelling. Any radiocarbon dated depths are calibrated. Age-depth models are constructed by sampling repeatedly from the dated levels, each time drawing age-depth curves. Model types include linear interpolation, linear or polynomial regression, and a range of splines. See Blaauw (2010). <doi:10.1016/j.quageo.2010.01.002>.
	"""
	
	cran = "clam" 

	version("2.5.0", md5="4b80c05ac3f917744e850ff5ded44fe7")

	depends_on("r-rintcal@0.4.1:", type=("build", "run"))
