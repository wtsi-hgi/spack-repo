# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvestr(RPackage):
	"""Inverse Estimation/Calibration Functions

	Functions to facilitate inverse estimation (e.g., calibration) in
    linear, generalized linear, nonlinear, and (linear) mixed-effects models. A
    generic function is also provided for plotting fitted regression models with
    or without confidence/prediction bands that may be of use to the general
    user. For a general overview of these methods, see Greenwell and Schubert 
    Kabban (2014) <doi:10.32614/RJ-2014-009>.
	"""
	
	homepage = "https://github.com/bgreenwell/investr"
	cran = "investr" 

	version("1.4.2", md5="35f482b245f8033f4168e87d4a02e898")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
