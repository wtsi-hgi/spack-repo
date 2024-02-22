# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkdescr(RPackage):
	"""Descriptive Statistics

	Computation of standardized interquartile range (IQR), Huber-type skipped mean (Hampel (1985), <doi:10.2307/1268758>), robust coefficient of variation (CV) (Arachchige et al. (2019), <arXiv:1907.01110>), robust signal to noise ratio (SNR), z-score, standardized mean difference (SMD), as well as functions that support graphical visualization such as boxplots based on quartiles (not hinges), negative logarithms and generalized logarithms for 'ggplot2' (Wickham (2016), ISBN:978-3-319-24277-4).
	"""
	
	homepage = "https://github.com/stamats/MKdescr"
	cran = "MKdescr" 

	version("0.8", md5="2a3584a6fd07d10d2781de1e2ec8577e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
