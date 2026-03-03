# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RButcher(RPackage):
	"""Model Butcher

	Provides a set of S3 generics to axe components of fitted
    model objects and help reduce the size of model objects saved to disk.
	"""
	
	homepage = "https://butcher.tidymodels.org/"
	cran = "butcher" 

	version("0.3.3", md5="2a573412b864064cf44fb6a1340bece9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-lobstr@1.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-vctrs@0.4.1:", type=("build", "run"))
