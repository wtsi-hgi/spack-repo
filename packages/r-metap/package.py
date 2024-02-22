# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetap(RPackage):
	"""Meta-Analysis of Significance Values.

	The canonical way to perform meta-analysis involves using effect sizes.
	When they are not available this package provides a number of methods for
	meta-analysis of significance values including the methods of Edgington,
	Fisher, Lancaster, Stouffer, Tippett, and Wilkinson; a number of data-sets
	to replicate published results; and a routine for graphical display."""

	cran = "metap"

	version("1.9", md5="56a203f1459ed188dd3329bb9268f0d6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-tfisher", type=("build", "run"))
	depends_on("r-mutoss", type=("build", "run"))
	depends_on("r-mathjaxr@0.8.3:", type=("build", "run"))
	depends_on("r-qqconf", type=("build", "run"))
