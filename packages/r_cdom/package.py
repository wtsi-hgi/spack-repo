# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdom(RPackage):
	"""R Functions to Model CDOM Spectra

	Wrapper functions to model and extract various quantitative information from absorption spectra of chromophoric dissolved organic matter (CDOM).
	"""
	
	homepage = "https://github.com/PMassicotte/cdom"
	cran = "cdom" 

	version("0.1.0", md5="c18f05fb6ec694dff7f3fc413b247dc9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
