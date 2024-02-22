# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBelg(RPackage):
	"""Boltzmann Entropy of a Landscape Gradient

	Calculates the Boltzmann entropy of a landscape gradient.
    This package uses the analytical method created by Gao, P., Zhang, H.
    and Li, Z., 2018 (<doi:10.1111/tgis.12315>) and by Gao, P. and Li, Z., 2019
    (<doi:10.1007/s10980-019-00854-3>). It also extend the original ideas by
    allowing calculations on data with missing values.
	"""
	
	homepage = "https://r-spatialecology.github.io/belg/"
	cran = "belg" 

	version("1.5.3", md5="b990075866874de6617299ea79994f32")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
