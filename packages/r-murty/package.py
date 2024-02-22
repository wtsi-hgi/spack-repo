# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMurty(RPackage):
	"""Murty's Algorithm for k-Best Assignments

	Calculates k-best solutions and costs for an assignment problem following the method outlined in Murty (1968) <doi:10.1287/opre.16.3.682>.
	"""
	
	homepage = "https://github.com/arg0naut91/muRty"
	cran = "muRty" 

	version("0.3.1", md5="9fdf84af4a492e62f7de2faa70823c93")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
