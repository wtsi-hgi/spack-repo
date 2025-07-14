# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClst(RPackage):
	"""Classification by local similarity threshold

	Package for modified nearest-neighbor classification based on calculation of a similarity threshold distinguishing within-group from between-group comparisons.
	"""
	
	bioc = "clst"

	version("1.56.0", commit="f51c525286f64afe0239137018b3f98157333b78")
	version("1.50.0", commit="203089bc3ad9756e4e188ade216f00166f686dc1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-roc", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
