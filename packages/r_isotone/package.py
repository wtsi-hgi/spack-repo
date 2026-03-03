# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsotone(RPackage):
	"""Active Set and Generalized PAVA for Isotone Optimization

	Contains two main functions: one for
        solving general isotone regression problems using the
        pool-adjacent-violators algorithm (PAVA); another one provides
        a framework for active set methods for isotone optimization
        problems with arbitrary order restrictions. Various types of
        loss functions are prespecified.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/psychor/"
	cran = "isotone" 

	version("1.1-1", md5="b735523b6a89a64d79b9ebae36138fbd")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
