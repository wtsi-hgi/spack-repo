# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXposeNlmixr2(RPackage):
	"""Graphical Diagnostics for Pharmacometric Models: Extension to
'nlmixr2'

	Extension to 'xpose' to support 'nlmixr2'. Provides functions to import 'nlmixr2' fit data into an 'xpose' data object, allowing the use of 'xpose' for 'nlmixr2' model diagnostics.
	"""
	
	cran = "xpose.nlmixr2" 

	version("0.4.0", md5="80fd9987fafd850a5817766e3d64eded", url="https://cran.r-project.org/src/contrib/xpose.nlmixr2_0.4.0.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-xpose@0.4.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tidyr@0.7.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-vpc@1.0.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-nlmixr2est", type=("build", "run"))
