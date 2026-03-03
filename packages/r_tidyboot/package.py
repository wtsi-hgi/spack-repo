# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyboot(RPackage):
	"""Tidyverse-Compatible Bootstrapping

	Compute arbitrary non-parametric bootstrap statistics on data in
    tidy data frames.
	"""
	
	homepage = "https://github.com/langcog/tidyboot"
	cran = "tidyboot" 

	version("0.1.1", md5="1f3029ebf672f5948f7b610c8f620f8b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-modelr@0.1.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-rlang@0.1.6:", type=("build", "run"))
	depends_on("r-tidyr@0.7.2:", type=("build", "run"))
