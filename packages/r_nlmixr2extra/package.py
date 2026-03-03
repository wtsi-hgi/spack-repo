# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmixr2extra(RPackage):
	"""Nonlinear Mixed Effects Models in Population PK/PD, Extra
Support Functions

	Fit and compare nonlinear mixed-effects models in
    differential equations with flexible dosing information commonly seen
    in pharmacokinetics and pharmacodynamics (Almquist, Leander, and
    Jirstrand 2015 <doi:10.1007/s10928-015-9409-1>). Differential equation
    solving is by compiled C code provided in the 'rxode2' package (Wang,
    Hallow, and James 2015 <doi:10.1002/psp4.12052>). This package is for
    support functions like preconditioned fits
    <doi:10.1208/s12248-016-9866-5>, boostrap and stepwise covariate
    selection.
	"""
	
	homepage = "https://nlmixr2.github.io/nlmixr2extra/"
	cran = "nlmixr2extra" 

	version("2.0.9", md5="2bae2e42f560a2683eb9ed80b2ce7175")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lotri", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-nlmixr2est@2.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rxode2@2.0.10:", type=("build", "run"))
	depends_on("r-symengine", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
