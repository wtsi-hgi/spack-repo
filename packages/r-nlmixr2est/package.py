# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmixr2est(RPackage):
	"""Nonlinear Mixed Effects Models in Population PK/PD, Estimation
Routines

	Fit and compare nonlinear mixed-effects models in
    differential equations with flexible dosing information commonly seen
    in pharmacokinetics and pharmacodynamics (Almquist, Leander, and
    Jirstrand 2015 <doi:10.1007/s10928-015-9409-1>). Differential equation
    solving is by compiled C code provided in the 'rxode2' package (Wang,
    Hallow, and James 2015 <doi:10.1002/psp4.12052>).
	"""
	
	homepage = "https://github.com/nlmixr2/nlmixr2est"
	cran = "nlmixr2est" 

	version("2.2.1", md5="a7462867788414d1c5943b55ebdf7200")

	depends_on("r-nlmixr2data", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lbfgsb3c", type=("build", "run"))
	depends_on("r-lotri", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-n1qn1@6.0.1.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-rxode2@2.0.12:", type=("build", "run"))
	depends_on("r-symengine", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.11.2.3.1:", type=("build", "run"))
	depends_on("r-rxode2parse@2.0.11:", type=("build", "run"))
	depends_on("r-rxode2random@2.0.9:", type=("build", "run"))
