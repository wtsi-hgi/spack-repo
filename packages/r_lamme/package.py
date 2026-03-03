# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLamme(RPackage):
	"""Log-Analytic Methods for Multiplicative Effects

	Log-analytic methods intended for testing multiplicative effects.
	"""
	
	cran = "lamme" 

	version("0.0.1", md5="450c18e63cda1e2a52a37e4d00be88a2")

	depends_on("r@3.4:", type=("build", "run"))
