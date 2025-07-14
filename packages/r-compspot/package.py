# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompspot(RPackage):
	"""compSPOT: Tool for identifying and comparing significantly mutated genomic hotspots

	Clonal cell groups share common mutations within cancer, precancer, and even clinically normal appearing tissues. The frequency and location of these mutations may predict prognosis and cancer risk. It has also been well established that certain genomic regions have increased sensitivity to acquiring mutations. Mutation-sensitive genomic regions may therefore serve as markers for predicting cancer risk. This package contains multiple functions to establish significantly mutated hotspots, compare hotspot mutation burden between samples, and perform exploratory data analysis of the correlation between hotspot mutation burden and personal risk factors for cancer, such as age, gender, and history of carcinogen exposure. This package allows users to identify robust genomic markers to help establish cancer risk.
	"""
	
	homepage = "https://github.com/sydney-grant/compSPOT"
	bioc = "compSPOT"

	version("1.6.0", commit="a664e3ca3f02db7e9c97597ebdabb422cb2ee840")
	version("1.0.0", commit="d769f5fcf923047e178263a1fa6629d77a5105c2")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
