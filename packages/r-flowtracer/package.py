# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowtracer(RPackage):
	"""Tracing Information Flow for Inter-Software Comparisons in Mass
Spectrometry-Based Bottom-Up Proteomics

	Useful functions to standardize software outputs from ProteomeDiscoverer, Spectronaut, DIA-NN and MaxQuant on precursor, modified peptide and proteingroup level and to trace software differences for identifications such as varying proteingroup denotations for common precursor.
	"""
	
	homepage = "https://github.com/OKdll/flowTraceR"
	cran = "flowTraceR" 

	version("0.1.0", md5="270d1e5cee33c25e48a948a8335341a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-comprehenr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
