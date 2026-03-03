# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvasioncorrection(RPackage):
	"""Invasion Correction

	The correction is achieved under the assumption that non-migrating cells of the essay approximately form a quadratic flow profile due to frictional effects, compare law of Hagen-Poiseuille for flow in a tube. The script fits a conical plane to give xyz-coordinates of the cells. It outputs the number of migrated cells and the new corrected coordinates.
	"""
	
	cran = "InvasionCorrection" 

	version("0.1", md5="3fddc664cad5aab3ff4f77ed09f2cbc5")

	depends_on("r-lattice", type=("build", "run"))
