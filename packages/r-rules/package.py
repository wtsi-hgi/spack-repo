# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRules(RPackage):
	"""Model Wrappers for Rule-Based Models

	Bindings for additional models for use with the 'parsnip'
    package.  Models include prediction rule ensembles (Friedman and
    Popescu, 2008) <doi:10.1214/07-AOAS148>, C5.0 rules (Quinlan, 1992
    ISBN: 1558602380), and Cubist (Kuhn and Johnson, 2013)
    <doi:10.1007/978-1-4614-6849-3>.
	"""
	
	homepage = "https://github.com/tidymodels/rules"
	cran = "rules" 

	version("1.0.2", md5="5ce341075d87bf87edc87dbc16f5fb6f")

	depends_on("r-parsnip@0.2.1.9004:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dials@0.1.1.9001:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics@0.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
