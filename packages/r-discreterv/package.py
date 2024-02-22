# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscreterv(RPackage):
	"""Create and Manipulate Discrete Random Variables

	Create, manipulate, transform, and simulate from discrete random
    variables. The syntax is modeled after that which is used in mathematical
    statistics and probability courses, but with powerful support for more
    advanced probability calculations. This includes the creation of joint
    random variables, and the derivation and manipulation of their conditional
    and marginal distributions.
	"""
	
	homepage = "https://github.com/erichare/discreteRV"
	cran = "discreteRV" 

	version("1.2.2", md5="198c7a02bb066d057a364e94ed25d4be")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
