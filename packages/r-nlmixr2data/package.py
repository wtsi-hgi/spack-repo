# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmixr2data(RPackage):
	"""Nonlinear Mixed Effects Models in Population PK/PD, Data

	Datasets for 'nlmixr2' and 'rxode2'. 'nlmixr2' is used for fitting and comparing
    nonlinear mixed-effects models in differential
    equations with flexible dosing information commonly seen in pharmacokinetics
    and pharmacodynamics (Almquist, Leander, and Jirstrand 2015
    <doi:10.1007/s10928-015-9409-1>). Differential equation solving is
    by compiled C code provided in the 'rxode2' package
    (Wang, Hallow, and James 2015 <doi:10.1002/psp4.12052>).
	"""
	
	homepage = "https://nlmixr2.github.io/nlmixr2data/"
	cran = "nlmixr2data" 

	version("2.0.9", md5="2bd2a4c4653bad3fab3f842e9e37d7b3")

	depends_on("r@2.10:", type=("build", "run"))
