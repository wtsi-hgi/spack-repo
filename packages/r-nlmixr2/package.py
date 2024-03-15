# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmixr2(RPackage):
	"""Nonlinear Mixed Effects Models in Population PK/PD

	Fit and compare nonlinear mixed-effects models in differential
    equations with flexible dosing information commonly seen in pharmacokinetics
    and pharmacodynamics (Almquist, Leander, and Jirstrand 2015
    <doi:10.1007/s10928-015-9409-1>). Differential equation solving is
    by compiled C code provided in the 'rxode2' package
    (Wang, Hallow, and James 2015 <doi:10.1002/psp4.12052>).
	"""
	
	homepage = "https://nlmixr2.org/"
	cran = "nlmixr2" 

	version("2.1.1", md5="8595a95a13d947158cfe05ca8f76c04a", url="https://cran.r-project.org/src/contrib/nlmixr2_2.1.1.tar.gz")

	depends_on("r-nlmixr2data", type=("build", "run"))
	depends_on("r-nlmixr2est@2.2:", type=("build", "run"))
	depends_on("r-nlmixr2extra", type=("build", "run"))
	depends_on("r-rxode2@2.1.1:", type=("build", "run"))
	depends_on("r-lotri", type=("build", "run"))
	depends_on("r-nlmixr2plot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
