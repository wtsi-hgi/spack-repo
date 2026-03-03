# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatirt(RPackage):
	"""Simulate IRT-Based Computerized Adaptive Tests

	Functions designed to simulate data that conform to basic
          unidimensional IRT models (for now 3-parameter binary response models
          and graded response models) along with Post-Hoc CAT simulations of
          those models given various item selection methods, ability estimation
          methods, and termination criteria. See
          Wainer (2000) <doi:10.4324/9781410605931>,
          van der Linden & Pashley (2010) <doi:10.1007/978-0-387-85461-8_1>,
          and Eggen (1999) <doi:10.1177/01466219922031365> for more details.
	"""
	
	homepage = "https://github.com/swnydick/catIrt"
	cran = "catIrt" 

	version("0.5.1", md5="ca8a90afb8be087dd297e54f8095024e")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-numderiv@2012.3.1:", type=("build", "run"))
