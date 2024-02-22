# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnestep(RPackage):
	"""One-Step Estimation

	Provide principally an eponymic function that numerically computes the Le Cam one-step estimator which is asymptotically efficient (see e.g. L. Le Cam (1956) <https://projecteuclid.org/euclid.bsmsp/1200501652>) and can be computed faster than the maximum likelihood estimator for large observation samples.
	"""
	
	cran = "OneStep" 

	version("0.9.2", md5="2f72fb82bdf4838e26a18f23536813b7")

	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
