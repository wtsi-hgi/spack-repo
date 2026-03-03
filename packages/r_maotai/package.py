# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaotai(RPackage):
	"""Tools for Matrix Algebra, Optimization and Inference

	Matrix is an universal and sometimes primary object/unit in applied mathematics and statistics. We provide a number of algorithms for selected problems in optimization and statistical inference. For general exposition to the topic with focus on statistical context, see the book by Banerjee and Roy (2014, ISBN:9781420095388).
	"""
	
	homepage = "https://github.com/kisungyou/maotai"
	cran = "maotai" 

	version("0.2.5", md5="b6f47057714e37993116fbce7ebe5f40")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-labdsv", type=("build", "run"))
	depends_on("r-shapes", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
