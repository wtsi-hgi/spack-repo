# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSandbox(RPackage):
	"""Probabilistic Numerical Modelling of Sediment Properties

	A flexible framework for definition and application of time/depth-
    based rules for sets of parameters for single grains that can be used to 
    create artificial sediment profiles. Such profiles can be used for virtual 
    sample preparation and synthetic, for instance, luminescence measurements.
	"""
	
	cran = "sandbox" 

	version("0.2.1", md5="fa206be6a5ec63d5e9f8178f0ca318f8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rlummodel@0.2.9:", type=("build", "run"))
