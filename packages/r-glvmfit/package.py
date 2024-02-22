# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlvmfit(RPackage):
	"""Methods to Assess Generalized Latent Variable Model Fit

	Provides residual global fit indices for generalized latent variable models. 
	"""
	
	cran = "glvmfit" 

	version("0.1.0", md5="5c71ef4180ea17e3a20ec06c5d90587f")

	depends_on("r@2.10:", type=("build", "run"))
