# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcs(RPackage):
	"""Calculate the Probability of Correct Selection (PCS)

	Given k populations (can be in thousands), what is the probability that a given subset of size t contains the true top t populations?  This package finds this probability and offers three tuning parameters (G, d, L) to relax the definition.
	"""
	
	cran = "PCS" 

	version("1.3", md5="2f9740b266ea801fd0282a6a13fceceb")

	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
