# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlpoly(RPackage):
	"""Random-Effect Multiple QTL Mapping in Autopolyploids

	Performs random-effect multiple interval mapping (REMIM) in full-sib families of autopolyploid species based on restricted maximum likelihood (REML) estimation and score statistics, as described in Pereira et al. (2020) <doi:10.1534/genetics.120.303080>.
	"""
	
	homepage = "https://gabrielgesteira.github.io/QTLpoly/"
	cran = "qtlpoly" 

	version("0.2.4", md5="dc0abbd618608aef4989aaee99af8dd5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-abind@1.4:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-gtools@3.9.2:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlrsim", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mappoly", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
