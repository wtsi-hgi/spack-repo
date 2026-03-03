# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmixr2plot(RPackage):
	"""Nonlinear Mixed Effects Models in Population PK/PD, Plot
Functions

	Fit and compare nonlinear mixed-effects models in
    differential equations with flexible dosing information commonly seen
    in pharmacokinetics and pharmacodynamics (Almquist, Leander, and
    Jirstrand 2015 <doi:10.1007/s10928-015-9409-1>). Differential equation
    solving is by compiled C code provided in the 'rxode2' package (Wang,
    Hallow, and James 2015 <doi:10.1002/psp4.12052>). This package is for
    'ggplot2' plotting methods for 'nlmixr2' objects.
	"""
	
	homepage = "https://github.com/nlmixr2/nlmixr2plot"
	cran = "nlmixr2plot" 

	version("2.0.8", md5="e9bf2089c4f71c70831f9011f2a16e02")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-nlmixr2est", type=("build", "run"))
	depends_on("r-nlmixr2extra", type=("build", "run"))
	depends_on("r-rxode2", type=("build", "run"))
	depends_on("r-vpc", type=("build", "run"))
	depends_on("r-xgxr", type=("build", "run"))
