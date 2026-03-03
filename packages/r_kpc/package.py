# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKpc(RPackage):
	"""Kernel Partial Correlation Coefficient

	Implementations of two empirical versions the kernel partial correlation (KPC) coefficient
    and the associated variable selection algorithms. KPC is a measure of the strength of conditional
    association between Y and Z given X, with X, Y, Z being random variables taking values in
    general topological spaces. As the name suggests, KPC is defined in terms of kernels on
    reproducing kernel Hilbert spaces (RKHSs). The population KPC is a deterministic number
    between 0 and 1; it is 0 if and only if Y is conditionally independent of Z given X, and it is 1 if
    and only if Y is a measurable function of Z and X. One empirical KPC estimator is based on
    geometric graphs, such as K-nearest neighbor graphs and minimum spanning trees, and is
    consistent under very weak conditions. The other empirical estimator, defined using conditional
    mean embeddings (CMEs) as used in the RKHS literature, is also consistent under suitable
    conditions. Using KPC, a stepwise forward variable selection algorithm KFOCI (using the graph
    based estimator of KPC) is provided, as well as a similar stepwise forward selection algorithm
    based on the RKHS based estimator. For more details on KPC, its empirical estimators and its
    application on variable selection, see Huang, Z., N. Deb, and B. Sen (2022). “Kernel partial
    correlation coefficient – a measure of conditional dependence” (URL listed below). When X is
    empty, KPC measures the unconditional dependence between Y and Z, which has been described
    in Deb, N., P. Ghosal, and B. Sen (2020), “Measuring association on topological spaces using
    kernels and geometric graphs” <arXiv:2010.01768>, and it is implemented in the functions
    KMAc() and Klin() in this package. The latter can be computed in near linear time.
	"""
	
	homepage = "https://www.jmlr.org/papers/v23/21-493.html"
	cran = "KPC" 

	version("0.1.2", md5="e899baed77f63ec2de843ebb50a8edcd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-mlpack", type=("build", "run"))
