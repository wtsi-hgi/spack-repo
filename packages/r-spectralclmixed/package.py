# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectralclmixed(RPackage):
	"""Spectral Clustering for Mixed Type Data

	Performs cluster analysis of mixed-type data using Spectral Clustering, see F. Mbuga and, C. Tortora (2022) <doi:10.3390/stats5010001>.
	"""
	
	cran = "SpectralClMixed" 

	version("1.0.1", md5="dbb5ec207eccc17eeed7726e371adf41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
