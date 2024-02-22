# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdaunif(RPackage):
	"""Uniform Manifold Samplers for Topological Data Analysis

	Uniform random samples from simple manifolds, sometimes with noise,
    are commonly used to test topological data analytic (TDA) tools.
    This package includes samplers powered by two techniques: analytic
    volume-preserving parameterizations, as employed by Arvo (1995)
    <doi:10.1145/218380.218500>, and rejection sampling, as employed by
    Diaconis, Holmes, and Shahshahani (2013) <doi:10.1214/12-IMSCOLL1006>.
	"""
	
	homepage = "https://tdaverse.github.io/tdaunif/"
	cran = "tdaunif" 

	version("0.1.1", md5="513c5225edcecff2e7b0be1f77e452c4")

	depends_on("r@3.3:", type=("build", "run"))
