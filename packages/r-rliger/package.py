# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRliger(RPackage):
	"""Linked Inference of Genomic Experimental Relationships

	Uses an extension of nonnegative matrix factorization to identify shared and dataset-specific factors. See Welch J, Kozareva V, et al (2019) <doi:10.1016/j.cell.2019.05.006>, and Liu J, Gao C, Sodicoff J, et al (2020) <doi:10.1038/s41596-020-0391-8> for more details.
	"""
	
	homepage = "https://github.com/welch-lab/liger"
	cran = "rliger" 

	version("1.0.1", md5="1ded96d6cdd656b1eeec4f7519fdf410")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-hdf5r", type=("build", "run"))
	depends_on("r-scattermore@0.7:", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
