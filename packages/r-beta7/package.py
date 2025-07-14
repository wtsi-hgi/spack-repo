# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeta7(RPackage):
	"""Rodriguez et al. (2004) Differential Gene Expression by Memory/Effector T Helper Cells Bearing the Gut-Homing Receptor Integrin alpha4 beta7.

	Data from 6 gpr files aims to identify differential expressed genes between the beta 7+ and beta 7- memory T helper cells.
	"""
	
	bioc = "beta7"

	version("1.46.0", commit="d1fcd5b674b4d2c8756adda43997a21bbd815e80")
	version("1.40.0", commit="ba9f40ce4a3208b188caa64a0bc0db1b9984d0d5")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))

