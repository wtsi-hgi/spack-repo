# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialkwd(RPackage):
	"""Spatial KWD for Large Spatial Maps

	Contains efficient implementations of Discrete Optimal Transport algorithms for the computation of Kantorovich-Wasserstein distances between pairs of large spatial maps (Bassetti, Gualandi, Veneroni (2020), <doi:10.1137/19M1261195>). All the algorithms are based on an ad-hoc implementation of the Network Simplex algorithm. The package has four main helper functions: compareOneToOne() (to compare two spatial maps), compareOneToMany() (to compare a reference map with a list of other maps), compareAll() (to compute a matrix of distances between a list of maps), and focusArea() (to compute the KWD distance within a focus area). In non-convex maps, the helper functions first build the convex-hull of the input bins and pad the weights with zeros.
	"""
	
	cran = "SpatialKWD" 

	version("0.4.1", md5="409b52cb9f42f8fe042b765683e8f333")

	depends_on("r-rcpp", type=("build", "run"))
