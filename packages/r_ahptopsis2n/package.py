# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhptopsis2n(RPackage):
	"""Hybrid Method for Multiple Criteria Decision-Making (MCDM)

	Implementation of a hybrid MCDM method build from the AHP (Analytic Hierarchy Process) and TOPSIS-2N (Technique for Order of Preference by Similarity to Ideal Solution - with two normalizations). This method is described in Souza et al. (2018) <doi: 10.1142/S0219622018500207>.
	"""
	
	cran = "ahptopsis2n" 

	version("0.2.0", md5="56277086899567730c5b77757d460845")

