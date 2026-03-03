# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrathe2e2(RPackage):
	"""End-to-End Marine Food Web Model

	A dynamic model of 
    the big-picture, whole ecosystem effects of hydrodynamics, 
	temperature, nutrients, and fishing on continental shelf marine 
	food webs. The package is described in: Heath, M.R., 
	Speirs, D.C., Thurlbeck, I. and Wilson, R.J. (2020) 
	<doi:10.1111/2041-210X.13510> StrathE2E2: An R package 
	for modelling the dynamics of marine food webs and 
	fisheries. 8pp.
	"""
	
	homepage = "https://gitlab.com/MarineResourceModelling/StrathE2E/StrathE2E2"
	cran = "StrathE2E2" 

	version("3.3.0", md5="b3565b37f3d11187b4085b68478892ec", url="https://cran.r-project.org/src/contrib/StrathE2E2_3.3.0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-netindices", type=("build", "run"))
