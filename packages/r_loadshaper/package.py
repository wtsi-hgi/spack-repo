# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoadshaper(RPackage):
	"""Producing Load Shape with Target Peak and Load Factor

	Modifying a load shape to match specific peak and 
  load factor is a fundamental component for various power system 
  planning and operation studies. This package is an efficient tool 
  to modify a reference load shape while matching the desired peak
  and load factor. The package offers both linear and non-linear method,
  described in <https://rpubs.com/riazakhan94/load_shape_match_peak_energy>. 
  The user can control the shape of the final load shape by regulating 
  certain parameters. The package provides validation metrics for 
  assessing the derived load shape in terms of preserving time series 
  properties. It also offers powerful graphics, that allows the user to
  visually assess the derived load shape.
	"""
	
	cran = "loadshaper" 

	version("1.1.1", md5="b98f0260609dd2635faaef8f279347f2")

	depends_on("r@2.10:", type=("build", "run"))
