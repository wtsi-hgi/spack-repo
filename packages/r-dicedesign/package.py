# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDicedesign(RPackage):
	"""Designs of Computer Experiments

	Space-Filling Designs and space-filling criteria (distance-based and uniformity-based), with emphasis to computer experiments; <doi:10.18637/jss.v065.i11>.
	"""
	
	cran = "DiceDesign" 

	version("1.10", md5="1006a4bae25c296e3ad5a60a62ed719c")

	depends_on("r@2.10:", type=("build", "run"))
