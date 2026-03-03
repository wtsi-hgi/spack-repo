# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychrolib(RPackage):
	"""Psychrometric Properties of Moist and Dry Air

	
    Implementation of 'PsychroLib'
    <https://github.com/psychrometrics/psychrolib> library which contains
    functions to enable the calculation properties of moist and dry air in both
    metric (SI) and imperial (IP) systems of units. References: Meyer, D. and
    Thevenard, D (2019) <doi:10.21105/joss.01137>.
	"""
	
	homepage = "https://github.com/psychrometrics/psychrolib"
	cran = "psychrolib" 

	version("2.5.2", md5="b27bac5e89acdb8f53fd45c6fad6fe87")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
