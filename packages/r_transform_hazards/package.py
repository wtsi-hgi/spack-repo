# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransformHazards(RPackage):
	"""Transforms Cumulative Hazards to Parameter Specified by ODE
System

	Targets parameters that solve Ordinary Differential
    Equations (ODEs) driven by a vector of cumulative hazard functions.
    The package provides a method for estimating these parameters using
    an estimator defined by a corresponding Stochastic Differential Equation
    (SDE) system driven by cumulative hazard estimates. By providing cumulative
    hazard estimates as input, the package gives estimates of the parameter as
    output, along with pointwise (co)variances derived from an asymptotic
    expression. Examples of parameters that can be targeted in this way include
    the survival function, the restricted mean survival function, cumulative
    incidence functions, among others; see Ryalen, Stensrud, and Røysland (2018)
    <doi:10.1093/biomet/asy035>, and further applications in
    Stensrud, Røysland, and Ryalen (2019) <doi:10.1111/biom.13102>
    and Ryalen et al. (2021) <doi:10.1093/biostatistics/kxab009>.
	"""
	
	cran = "transform.hazards" 

	version("0.1.1", md5="97a2f37c68fb485e9206a3ac77cdaa30")

