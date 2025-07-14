# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpktools(RPackage):
	"""Methods for Spike-in Arrays

	The package contains functions that can be used to compare expression measures on different array platforms.
	"""
	
	homepage = "http://bioconductor.org"
	bioc = "spkTools"

	version("1.64.0", commit="62162cebca562c8dfa705954bbd368952981af64")
	version("1.58.0", commit="517c37a2ef1e6b12bd37a12f2d9abacb93422804")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
