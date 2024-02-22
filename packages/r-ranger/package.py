# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRanger(RPackage):
	"""A Fast Implementation of Random Forests.

	A fast implementation of Random Forests, particularly suited for high
	dimensional data. Ensembles of classification, regression, survival and
	probability prediction trees are supported. Data from genome-wide
	association studies can be analyzed efficiently. In addition to data
	frames, datasets of class 'gwaa.data' (R package 'GenABEL') and 'dgCMatrix'
	(R package 'Matrix') can be directly analyzed."""

	cran = "ranger"

	version("0.16.0", md5="813881b35ed050bcab58c5e92826c0f2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
