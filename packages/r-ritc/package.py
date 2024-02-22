# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRitc(RPackage):
	"""Isothermal Titration Calorimetry (ITC) Data Analysis

	Implements the simulation and regression of
        integrated Isothermal Titration Calorimetry (ITC) data using
        the most commonly used one-to-one binding reaction model.
	"""
	
	cran = "Ritc" 

	version("1.0.2", md5="aafb9574e1e4add3f894ca8f6aebf3cb")

	depends_on("r-minpack-lm", type=("build", "run"))
