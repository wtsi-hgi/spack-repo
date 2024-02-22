# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsn(RPackage):
	"""Closed Skew-Normal Distribution

	Provides functions for computing the density
    and the log-likelihood function of closed-skew normal variates,
    and for generating random vectors sampled from this distribution.
    See Gonzalez-Farias, G., Dominguez-Molina, J., and Gupta, A. (2004).
    The closed skew normal distribution, 
    Skew-elliptical distributions and their applications: a journey beyond normality,
    Chapman and Hall/CRC, Boca Raton, FL, pp. 25-42.
	"""
	
	cran = "csn" 

	version("1.1.3", md5="3ce2767e2c7b737ce454d4b6793784ff")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
