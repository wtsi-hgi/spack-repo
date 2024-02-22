# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatcpp(RPackage):
	"""Fast C++ Primitives for the 'NeuroAnatomy Toolbox'

	Fast functions implemented in C++ via 'Rcpp' to support the
    'NeuroAnatomy Toolbox' ('nat') ecosystem. These functions provide large
    speed-ups for basic manipulation of neuronal skeletons over pure R
    functions found in the 'nat' package. The expectation is that end
    users will not use this package directly, but instead the 'nat'
    package will automatically use routines from this package when it is
    available to enable large performance gains.
	"""
	
	homepage = "https://github.com/natverse/natcpp"
	cran = "natcpp" 

	version("0.1.0", md5="abf55cf060b0fe825a172d64bd06d7c8")

	depends_on("r-rcpp", type=("build", "run"))
