# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamc(RPackage):
	"""Spatial Absorbing Markov Chains

	Implements functions for working with absorbing Markov chains. The
    implementation is based on the framework described in "Toward a unified
    framework for connectivity that disentangles movement and mortality in space
    and time" by Fletcher et al. (2019) <doi:10.1111/ele.13333>, which applies
    them to spatial ecology. This framework incorporates both resistance and 
    absorption with spatial absorbing Markov chains (SAMC) to provide several
    short-term and long-term predictions for metrics related to connectivity in 
    landscapes. Despite the ecological context of the framework, this package
    can be used in any application of absorbing Markov chains.
	"""
	
	homepage = "https://andrewmarx.github.io/samc/"
	cran = "samc" 

	version("3.2.1", md5="d5a85826f870a2fd9b442e13777eec75")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.5.3:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-terra@1.7.3:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.3:", type=("build", "run"))
	depends_on("r-rcppthread@2.1.3:", type=("build", "run"))
