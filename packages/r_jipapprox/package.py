# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJipapprox(RPackage):
	"""Approximate Inclusion Probabilities for Survey Sampling

	Approximate joint-inclusion probabilities in Unequal Probability Sampling, or compute Monte Carlo approximations of the first and second-order inclusion probabilities of a general sampling design as in Fattorini (2006) <doi:10.1093/biomet/93.2.269>.
	"""
	
	cran = "jipApprox" 

	version("0.1.5", md5="8866af9fa21854929fd27c4a98999bb8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
