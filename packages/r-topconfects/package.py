# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopconfects(RPackage):
	"""Top Confident Effect Sizes

	Rank results by confident effect sizes, while maintaining False Discovery Rate and False Coverage-statement Rate control. Topconfects is an alternative presentation of TREAT results with improved usability, eliminating p-values and instead providing confidence bounds. The main application is differential gene expression analysis, providing genes ranked in order of confident log2 fold change, but it can be applied to any collection of effect sizes with associated standard errors.
	"""
	
	homepage = "https://github.com/pfh/topconfects"
	bioc = "topconfects"

	version("1.24.0", commit="8d72f5588ce59514e5eacefa775c4eabd1660b76")
	version("1.18.0", commit="b70aef24efd13521f872f9251cad3d061f54e18e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
