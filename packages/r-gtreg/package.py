# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtreg(RPackage):
	"""Regulatory Tables for Clinical Research

	Creates tables suitable for regulatory agency submission by
    leveraging the 'gtsummary' package as the back end. Tables can be exported
    to HTML, Word, PDF and more. Highly customized outputs are
    available by utilizing existing styling functions from 'gtsummary' as
    well as custom options designed for regulatory tables.
	"""
	
	homepage = "https://github.com/shannonpileggi/gtreg"
	cran = "gtreg" 

	version("0.3.0", md5="091472ce5f64cf06cb51673efed02831")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-broom-helpers@1.13:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-gtsummary@1.7.1:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.2.1:", type=("build", "run"))
