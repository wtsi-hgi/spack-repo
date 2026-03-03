# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBonsai(RPackage):
	"""Model Wrappers for Tree-Based Models

	Bindings for additional tree-based model engines for use with
    the 'parsnip' package. Models include gradient boosted decision trees
    with 'LightGBM' (Ke et al, 2017.) and
    conditional inference trees and conditional random forests with
    'partykit' (Hothorn and Zeileis, 2015. and
    Hothorn et al, 2006. <doi:10.1198/106186006X133933>).
	"""
	
	homepage = "https://bonsai.tidymodels.org/"
	cran = "bonsai" 

	version("0.2.1", md5="c53a983564c6c18d7d0e1ac8672a1cca")

	depends_on("r-parsnip@1.0.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
