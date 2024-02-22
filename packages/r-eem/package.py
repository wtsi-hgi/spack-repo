# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REem(RPackage):
	"""Read and Preprocess Fluorescence Excitation-Emission Matrix
(EEM) Data

	Read raw EEM data and prepares them for further analysis.
	"""
	
	homepage = "https://github.com/chengvt/EEM"
	cran = "EEM" 

	version("1.1.1", md5="3c682078d23053f4f9fd7de2bc673c78")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
