# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefund(RPackage):
	"""Regression with Functional Data

	Methods for regression for functional
    data, including function-on-scalar, scalar-on-function, and
    function-on-function regression. Some of the functions are applicable to
    image data.
	"""
	
	homepage = "https://github.com/refunders/refund"
	cran = "refund" 

	version("0.1-35", md5="5b120517d45554217e125ea92517a9bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mgcv@1.9:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rlrsim", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbs", type=("build", "run"))
