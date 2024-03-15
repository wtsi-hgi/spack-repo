# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIai(RPackage):
	"""Interface to 'Interpretable AI' Modules

	An interface to the algorithms of 'Interpretable AI'
    <https://www.interpretable.ai> from the R programming language.
    'Interpretable AI' provides various modules, including 'Optimal Trees' for
    classification, regression, prescription and survival analysis, 'Optimal
    Imputation' for missing data imputation and outlier detection, and 'Optimal
    Feature Selection' for exact sparse regression. The 'iai' package is an
    open-source project. The 'Interpretable AI' software modules are proprietary
    products, but free academic and evaluation licenses are available.
	"""
	
	homepage = "https://www.interpretable.ai"
	cran = "iai" 

	version("1.10.0", md5="6ad11993fdd4ccec1f38ae64400351fc")

	depends_on("r-juliacall@0.17.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("julia@1.0:", type=("build", "link", "run"))
