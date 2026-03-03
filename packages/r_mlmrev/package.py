# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmrev(RPackage):
	"""Examples from Multilevel Modelling Software Review

	Data and examples from a multilevel modelling software review
  as well as other well-known data sets from the multilevel modelling
  literature.
	"""
	
	cran = "mlmRev" 

	version("1.0-8", md5="f4d61472c9dd70d0cfc7f31b8a046aa0")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
