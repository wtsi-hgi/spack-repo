# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoeWrapper(RPackage):
	"""Wrapper Package for Design of Experiments Functionality

	Various kinds of designs for
 (industrial) experiments can be created. The package uses, and sometimes enhances,
        design generation routines from other packages. 
        So far, response surface designs from package 'rsm', Latin hypercube
        samples from packages 'lhs' and 'DiceDesign', and 
        D-optimal designs from package 'AlgDesign' have been implemented.
	"""
	
	homepage = "https://prof.bht-berlin.de/groemping/DoE/"
	cran = "DoE.wrapper" 

	version("0.12", md5="2fecbf3bbfc846cd5e48593744b271bb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-frf2@1.6.5:", type=("build", "run"))
	depends_on("r-doe-base@0.23.4:", type=("build", "run"))
	depends_on("r-rsm", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-dicedesign", type=("build", "run"))
	depends_on("r-algdesign@1.1:", type=("build", "run"))
