# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmccsd(RPackage):
	"""Efficient Estimation of Clustered Current Status Data

	Current status data abounds
            in the field of epidemiology and public health, where the only observable data for a subject is
            the random inspection time and the event status at inspection. Motivated by such a current status
            data from a periodontal study where data are inherently clustered,
            we propose a unified methodology to analyze such complex data.
	"""
	
	cran = "FMCCSD" 

	version("1.0", md5="b1b6117d066d2d9d03e025ed54e6a418")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
