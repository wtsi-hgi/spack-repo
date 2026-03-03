# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRotasym(RPackage):
	"""Tests for Rotational Symmetry on the Hypersphere

	Implementation of the tests for rotational symmetry on the
    hypersphere proposed in García-Portugués, Paindaveine and Verdebout (2020)
    <doi:10.1080/01621459.2019.1665527>. The package also implements the
    proposed distributions on the hypersphere, based on the tangent-normal
    decomposition, and allows for the replication of the data application
    considered in the paper.
	"""
	
	homepage = "https://github.com/egarpor/rotasym"
	cran = "rotasym" 

	version("1.1.5", md5="b09c85a93cf0781b97e6cdac4c22d1f9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
