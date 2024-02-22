# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvmethod(RPackage):
	"""Radial Velocity Method for Detecting Exoplanets

	Has various functions designed to implement the 
    Hermite-Gaussian Radial Velocity (HGRV) estimation approach of 
    Holzer et al. (2020) <arXiv:2005.14083>, which is a particular application of the radial 
    velocity method for detecting exoplanets. The overall approach consists 
    of four sequential steps, each of which has a function in this package: 
    (1) estimate the template spectrum with the function estimate_template(), 
    (2) find absorption features in the estimated template with the function 
    findabsorptionfeatures(), (3) fit Gaussians to the absorption features 
    with the function Gaussfit(), (4) apply the HGRV with simple linear 
    regression by calling the function hgrv(). This package is meant to be 
    open source. But please cite the paper Holzer et al. (2020) <arXiv:2005.14083> when 
    publishing results that use this package.
	"""
	
	cran = "rvmethod" 

	version("0.1.2", md5="ab6fb4b4c5365379195c6ec88d139608")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
