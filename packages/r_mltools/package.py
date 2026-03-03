# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMltools(RPackage):
	"""Machine Learning Tools

	A collection of machine learning helper functions, particularly assisting in the Exploratory Data Analysis phase. Makes heavy use of the 'data.table' package for optimal speed and memory efficiency. Highlights include a versatile bin_data() function, sparsify() for converting a data.table to sparse matrix format with one-hot encoding, fast evaluation metrics, and empirical_cdf() for calculating empirical Multivariate Cumulative Distribution Functions.
	"""
	
	homepage = "https://github.com/ben519/mltools"
	cran = "mltools" 

	version("0.3.5", md5="a27838eb72d1a9f9b9c7a922ac7efe7a")

	depends_on("r-data-table@1.9.7:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
