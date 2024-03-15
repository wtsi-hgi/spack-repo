# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRena(RPackage):
	"""Epistemic Network Analysis

	ENA (Shaffer, D. W. (2017) Quantitative Ethnography. ISBN: 0578191687) is a method used to identify meaningful and quantifiable patterns in discourse or reasoning. ENA moves beyond the traditional frequency-based assessments by examining the structure of the co-occurrence, or connections in coded data. Moreover, compared to other methodological approaches, ENA has the novelty of (1) modeling whole networks of connections and (2) affording both quantitative and qualitative comparisons between different network models.   Shaffer, D.W., Collier, W., & Ruis, A.R. (2016).
	"""
	
	homepage = "https://gitlab.com/epistemic-analytics/qe-packages/rENA"
	cran = "rENA" 

	version("0.2.7", md5="b0b1c75d802e43d31cc7b349fef3812f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-concatenate", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
