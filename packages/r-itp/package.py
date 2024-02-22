# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItp(RPackage):
	"""The Interpolate, Truncate, Project (ITP) Root-Finding Algorithm

	Implements the Interpolate, Truncate, Project (ITP) root-finding 
    algorithm developed by Oliveira and Takahashi (2021) <doi:10.1145/3423597>.
    The user provides the function, from the real numbers to the real numbers, 
    and an interval with the property that the values of the function at its 
    endpoints have different signs. If the function is continuous over this 
    interval then the ITP method estimates the value at which the function is 
    equal to zero. If the function is discontinuous then a point of 
    discontinuity at which the function changes sign may be found. 
    The function can be supplied using either an R function or an external 
    pointer to a C++ function. Tuning parameters of the ITP algorithm can be 
    set by the user. Default values are set based on arguments in Oliveira and 
    Takahashi (2021). 
	"""
	
	homepage = "https://paulnorthrop.github.io/itp/"
	cran = "itp" 

	version("1.2.1", md5="d3a48f476f8c04bcb1a713715c466d04")

	depends_on("r-rcpp", type=("build", "run"))
