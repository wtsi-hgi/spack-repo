# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTangledfeatures(RPackage):
	"""Feature Selection in Highly Correlated Spaces

	Feature selection algorithm that extracts features in highly
    correlated spaces. The extracted features are meant to be fed into
    simple explainable models such as linear or logistic regressions. The
    package is useful in the field of explainable modelling as a
    way to understand variable behavior.
	"""
	
	homepage = "https://allen-1242.github.io/TangledFeatures/"
	cran = "TangledFeatures" 

	version("0.1.1", md5="af7b3405b28b593e77bfaed0c0ccceec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-correlation", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
