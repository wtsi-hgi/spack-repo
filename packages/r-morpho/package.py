# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorpho(RPackage):
	"""Calculations and Visualisations Related to Geometric
Morphometrics

	A toolset for Geometric Morphometrics and mesh processing. This
    includes (among other stuff) mesh deformations based on reference points,
    permutation tests, detection of outliers, processing of sliding
    semi-landmarks and semi-automated surface landmark placement.
	"""
	
	homepage = "https://github.com/zarquon42b/Morpho"
	cran = "Morpho" 

	version("2.12", md5="7c56d57f526dcd49272f57d4fd5c779a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rvcg@0.7:", type=("build", "run"))
	depends_on("r-rgl@0.100.18:", type=("build", "run"))
	depends_on("r-foreach@1.4:", type=("build", "run"))
	depends_on("r-matrix@1.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-doparallel@1.0.6:", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-bezier", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4:", type=("build", "run"))
