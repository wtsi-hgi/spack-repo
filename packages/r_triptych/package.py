# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriptych(RPackage):
	"""Diagnostic Graphics to Evaluate Forecast Performance

	Overall predictive performance is measured by a mean score
    (or loss), which decomposes into miscalibration, discrimination, and
    uncertainty components. The main focus is visualization of these distinct
    and complementary aspects in joint displays.
    See Dimitriadis, Gneiting, Jordan, Vogel (2023) <arXiv:2301.10803>.
	"""
	
	homepage = "https://github.com/aijordan/triptych/"
	cran = "triptych" 

	version("0.1.2", md5="0d525a19eafb18d418da3de3fd4e63ea")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-monotone", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-geomtextpath", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
