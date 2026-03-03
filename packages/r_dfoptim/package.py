# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfoptim(RPackage):
	"""Derivative-Free Optimization

	Derivative-Free optimization algorithms. These algorithms do not require gradient information. More importantly, they can be used to solve non-smooth optimization problems.
	"""
	
	cran = "dfoptim" 

	version("2023.1.0", md5="fa0cc871a9d611318ecf2e1f671f10a6")

	depends_on("r@2.10.1:", type=("build", "run"))
