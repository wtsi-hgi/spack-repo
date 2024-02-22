# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRipserr(RPackage):
	"""Calculate Persistent Homology with Ripser-Based Engines

	Ports the Ripser <arXiv:1908.02518> and Cubical Ripser
        <arXiv:2005.12692> persistent homology calculation engines from
        C++. Can be used as a rapid calculation tool in topological
        data analysis pipelines.
	"""
	
	homepage = "https://rrrlw.github.io/ripserr/"
	cran = "ripserr" 

	version("0.1.1", md5="0bb8732f77f4d33361a35d422365926f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
