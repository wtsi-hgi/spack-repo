# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFer(RPackage):
	"""Financial Engineering in R

	R implementations of standard financial engineering codes;
  vanilla option pricing models such as Black-Scholes, Bachelier, CEV, and
  SABR.
	"""
	
	homepage = "https://github.com/PyFE/FE-R"
	cran = "FER" 

	version("0.94", md5="c924a7f3b999c772cfc406694e3bb150")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
