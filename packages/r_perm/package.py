# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerm(RPackage):
	"""Exact or Asymptotic Permutation Tests

	Perform Exact or Asymptotic permutation tests [see Fay and Shaw <doi:10.18637/jss.v036.i02>].
	"""
	
	cran = "perm" 

	version("1.0-0.4", md5="c95be15bed5a1b79cc5e4d1dd274c04a")

	depends_on("r@2.2.1:", type=("build", "run"))
