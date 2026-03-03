# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGexp(RPackage):
	"""Generator of Experiments

	Generates experiments - simulating structured or experimental data as: 
             completely randomized design, randomized block design, latin square design, 
             factorial and split-plot experiments (Ferreira, 2008, ISBN:8587692526; 
             Naes et al., 2007 <doi:10.1002/qre.841>; Rencher et al., 2007, ISBN:9780471754985; 
             Montgomery, 2001, ISBN:0471316490).
	"""
	
	homepage = "https://github.com/ivanalaman/gexp"
	cran = "gexp" 

	version("1.0-21", md5="3e1c8311bef9a9bf38231f93f0260d98")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
