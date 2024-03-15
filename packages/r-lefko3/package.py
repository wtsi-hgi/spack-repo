# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLefko3(RPackage):
	"""Historical and Ahistorical Population Projection Matrix Analysis

	Complete analytical environment for the construction and analysis
             of matrix population models and integral projection models.
             Includes the ability to construct historical matrices, which are
             2d matrices comprising 3 consecutive times of demographic
             information. Estimates both raw and function-based forms of
             historical and standard ahistorical matrices. It also estimates
             function-based age-by-stage matrices and raw and function-based
             Leslie matrices.
	"""
	
	homepage = "http://www.sheffersonlab.com/projects.html"
	cran = "lefko3" 

	version("6.2.1", md5="c1fc607b96f841c3bcf0f0de6f00b9a8", url="https://cran.r-project.org/src/contrib/lefko3_6.2.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
