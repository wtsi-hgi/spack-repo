# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastai(RPackage):
	"""Interface to 'fastai'

	The 'fastai' <https://docs.fast.ai/index.html> library 
             simplifies training fast and accurate neural networks 
             using modern best practices. It is based on research 
             in to deep learning best practices undertaken 
             at 'fast.ai', including 'out of the box' support
             for vision, text, tabular, audio, time series, and 
             collaborative filtering models. 
	"""
	
	homepage = "https://github.com/EagerAI/fastai"
	cran = "fastai" 

	version("2.2.1", md5="a73c8c16b540682f451d946299ae3d9c")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
