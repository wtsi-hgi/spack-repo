# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRliger(RPackage):
	"""Linked Inference of Genomic Experimental Relationships

	Uses an extension of nonnegative matrix factorization to identify shared and dataset-specific factors. See Welch J, Kozareva V, et al (2019) <doi:10.1016/j.cell.2019.05.006>, and Liu J, Gao C, Sodicoff J, et al (2020) <doi:10.1038/s41596-020-0391-8> for more details.
	"""
	
	homepage = "https://welch-lab.github.io/liger/"
	cran = "rliger" 

	version("2.0.0", md5="61f834cadad73c60fdd85d7dcd0b1426")
	version("1.0.1", md5="1ded96d6cdd656b1eeec4f7519fdf410")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hdf5r", type=("build", "run"))
	depends_on("r-leidenalg@1.1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
