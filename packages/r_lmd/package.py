# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmd(RPackage):
	"""A Self-Adaptive Approach for Demodulating Multi-Component Signal

	Local Mean Decomposition is an iterative and self-adaptive approach for demodulating, processing, and analyzing multi-component amplitude modulated and frequency modulated signals. This R package is based on the approach suggested by Smith (2005) <doi:10.1098/rsif.2005.0058> and the 'Python' library 'PyLMD'.
	"""
	
	homepage = "https://github.com/shubhra-opensource/LMD"
	cran = "LMD" 

	version("1.0.0", md5="287821fc4c37dfce2569d9f761cd6c58")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-emd", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
