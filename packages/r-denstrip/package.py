# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDenstrip(RPackage):
	"""Density Strips and Other Methods for Compactly Illustrating
Distributions

	Graphical methods for compactly illustrating probability distributions, including density strips, density regions, sectioned density plots and varying width strips.
	"""
	
	cran = "denstrip" 

	version("1.5.4", md5="71ac549af68bee3b8aa7b7dd7e5c3bdd")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
