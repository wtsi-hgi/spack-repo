# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSem(RPackage):
	"""Structural Equation Models

	Functions for fitting general linear structural
    equation models (with observed and latent variables) using the RAM approach, 
    and for fitting structural equations in observed-variable models by two-stage least squares.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "sem" 

	version("3.1-15", md5="e5f3e48d9d92b3d228fd1a8b757d5b33")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mi@0.9.99:", type=("build", "run"))
