# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtbary(RPackage):
	"""Barycenter Methods for Spatial Point Patterns

	Computes a point pattern in R^2 or on a graph that is representative of a collection of many data patterns. The result is an approximate barycenter (also known as Fréchet mean or prototype) based on a transport-transform metric. Possible choices include Optimal SubPattern Assignment (OSPA) and Spike Time metrics. Details can be found in Müller, Schuhmacher and Mateu (2020) <doi:10.1007/s11222-020-09932-y>.
	"""
	
	cran = "ttbary" 

	version("0.3-1", md5="f53bb0833b02e4573f52c6e249e9584f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat@3.0.0:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatstat-linnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
