# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonoclust(RPackage):
	"""Perform Monothetic Clustering with Extensions to Circular Data

	Implementation of the Monothetic Clustering
    algorithm (Chavent, 1998 <doi:10.1016/S0167-8655(98)00087-7>) on
    continuous data sets. A lot of extensions are included in the package,
    including applying Monothetic clustering on data sets with circular
    variables, visualizations with the results, and permutation and
    cross-validation based tests to support the decision on the number of
    clusters.
	"""
	
	homepage = "https://vinhtantran.github.io/monoClust/"
	cran = "monoClust" 

	version("1.2.1", md5="444b3c874ac4d51c586f23d5073197ec")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cluster@2.0.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-stringr@0.5:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
