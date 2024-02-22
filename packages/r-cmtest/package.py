# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmtest(RPackage):
	"""Conditional Moments Test

	Conditional moments test, as proposed by Newey (1985) <doi:10.2307/1911011 > and Tauchen (1985) <doi:10.1016/0304-4076(85)90149-6>, useful to detect specification violations for models estimated by maximum likelihood. Methods for probit and tobit models are provided.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "cmtest" 

	version("0.1-2", md5="606736458e5d481f0ade3aa4b24a5d4f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
