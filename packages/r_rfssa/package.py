# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfssa(RPackage):
	"""Functional Singular Spectrum Analysis

	Methods and tools for implementing functional singular spectrum analysis and related techniques.
	"""
	
	homepage = "https://github.com/haghbinh/Rfssa"
	cran = "Rfssa" 

	version("3.1.0", md5="37fc5e11192a304de362237240451824")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rssa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rainbow", type=("build", "run"))
	depends_on("r-ftsa", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
