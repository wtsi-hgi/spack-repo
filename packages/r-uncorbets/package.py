# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUncorbets(RPackage):
	"""Uncorrelated Bets via Minimum Torsion Algorithm

	Implements Minimum Torsion for portfolio diversification as
    described in Meucci, Attilio (2013) <doi:10.2139/ssrn.2276632>.
	"""
	
	homepage = "https://github.com/Reckziegel/uncorbets"
	cran = "uncorbets" 

	version("0.1.2", md5="9c2d94ca9193742b7fdb48753aa11abb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-nlcoptim@0.6:", type=("build", "run"))
