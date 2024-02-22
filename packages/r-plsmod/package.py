# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsmod(RPackage):
	"""Model Wrappers for Projection Methods

	Bindings for additional regression models for use with the
    'parsnip' package, including ordinary and spare partial least squares
    models for regression and classification (Rohart et al (2017)
    <doi:10.1371/journal.pcbi.1005752>).
	"""
	
	homepage = "https://plsmod.tidymodels.org"
	cran = "plsmod" 

	version("1.0.0", md5="9fd949a2583b8db4d950edc399abd154")

	depends_on("r-parsnip@0.2:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
