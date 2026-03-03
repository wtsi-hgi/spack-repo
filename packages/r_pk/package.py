# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPk(RPackage):
	"""Basic Non-Compartmental Pharmacokinetics

	Estimation of pharmacokinetic parameters using non-compartmental theory.
	"""
	
	cran = "PK" 

	version("1.3-6", md5="bd60e4660915307461e1765389166470")

	depends_on("r@2.2.1:", type=("build", "run"))
