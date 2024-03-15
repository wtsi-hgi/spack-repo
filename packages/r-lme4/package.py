# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLme4(RPackage):
	"""Linear Mixed-Effects Models using 'Eigen' and S4.

	Fit linear and generalized linear mixed-effects models. The models and
	their components are represented using S4 classes and methods. The core
	computational algorithms are implemented using the 'Eigen' C++ library for
	numerical linear algebra and 'RcppEigen' "glue"."""

	cran = "lme4"

	license("GPL-2.0-or-later")

	version("1.1-35.1", md5="b452706beaa895b70d874a8a0154f87d", url="https://cran.r-project.org/src/contrib/lme4_1.1-35.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-nlme@3.1.123:", type=("build", "run"))
	depends_on("r-minqa@1.1.15:", type=("build", "run"))
	depends_on("r-nloptr@1.0.4:", type=("build", "run"))
	depends_on("r-rcpp@0.10.5:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.4:", type=("build", "run"))
