# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTurbonorm(RPackage):
	"""A fast scatterplot smoother suitable for microarray normalization

	A fast scatterplot smoother based on B-splines with second-order difference penalty. Functions for microarray normalization of single-colour data i.e. Affymetrix/Illumina and two-colour data supplied as marray MarrayRaw-objects or limma RGList-objects are available.
	"""
	
	homepage = "http://www.humgen.nl/MicroarrayAnalysisGroup.html"
	bioc = "TurboNorm"

	version("1.56.0", commit="80d9217dde169e3097ca9251ddc08f9e5d24e52b")
	version("1.50.0", commit="925fb78762fb556a60d52b363645fc6acff11495")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-convert", type=("build", "run"))
	depends_on("r-limma@1.7:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
