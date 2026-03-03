# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmeta(RPackage):
	"""A Toolbox for Multivariate Meta-Analysis

	A toolbox for meta-analysis. This package includes: 1,a robust multivariate meta-analysis of continuous or binary outcomes; 2, a bivariate Egger's test for detecting small study effects; 3, Galaxy Plot: A New Visualization Tool of Bivariate Meta-Analysis Studies; 4, a bivariate T&F method accounting for publication bias in bivariate meta-analysis, based on symmetry of the galaxy plot. Hong C. et al(2020) <doi:10.1093/aje/kwz286>, Chongliang L. et al(2020) <doi:10.1101/2020.07.27.20161562>.
	"""
	
	homepage = "https://github.com/Penncil/xmeta"
	cran = "xmeta" 

	version("1.3.2", md5="b506322cd742021596ce2b12e81fc656")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-glmmml", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-mvmeta", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
