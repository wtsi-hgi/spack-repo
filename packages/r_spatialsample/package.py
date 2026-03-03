# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialsample(RPackage):
	"""Spatial Resampling Infrastructure

	Functions and classes for spatial resampling to use with the
    'rsample' package, such as spatial cross-validation (Brenning, 2012)
    <doi:10.1109/IGARSS.2012.6352393>. The scope of 'rsample' and
    'spatialsample' is to provide the basic building blocks for creating
    and analyzing resamples of a spatial data set, but neither package
    includes functions for modeling or computing statistics. The resampled
    spatial data sets created by 'spatialsample' do not contain much
    overhead in memory.
	"""
	
	homepage = "https://github.com/tidymodels/spatialsample"
	cran = "spatialsample" 

	version("0.5.1", md5="ca915f7b2051704e49848b3b1cfcc2f1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rsample@1.1.1:", type=("build", "run"))
	depends_on("r-sf@1.0.9:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-vctrs@0.3.6:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
