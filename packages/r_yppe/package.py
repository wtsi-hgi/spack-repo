# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYppe(RPackage):
	"""Yang and Prentice Model with Piecewise Exponential Baseline
Distribution

	Semiparametric modeling of lifetime data with crossing survival curves via Yang and Prentice model with piecewise exponential baseline distribution. Details about the model can be found in Demarqui and Mayrink (2019) <arXiv:1910.02406>. Model fitting carried out via likelihood-based and Bayesian approaches. The package also provides point and interval estimation for the crossing survival times.
	"""
	
	homepage = "https://github.com/fndemarqui/YPPE"
	cran = "YPPE" 

	version("1.0.1", md5="441d14649a12c32c15c795b4d9de047e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
