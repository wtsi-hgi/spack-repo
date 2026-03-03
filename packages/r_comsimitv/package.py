# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComsimitv(RPackage):
	"""Flexible Framework for Simulating Community Assembly

	Flexible framework for trait-based simulation of community assembly, where components could be replaced by user-defined function and that
             allows variation of traits within species.
	"""
	
	cran = "comsimitv" 

	version("0.1.5", md5="f9361e68936e3306d40d96707a58cc6c")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
