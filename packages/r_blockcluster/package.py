# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockcluster(RPackage):
	"""Co-Clustering Package for Binary, Categorical, Contingency and
Continuous Data-Sets

	Simultaneous clustering of rows and columns, usually designated by
    biclustering, co-clustering or block clustering, is an important technique
    in two way data analysis. It consists of estimating a mixture model which
    takes into account the block clustering problem on both the individual and
    variables sets. The 'blockcluster' package provides a bridge between the C++
    core library build on top of the 'STK++' library, and the R statistical
    computing environment. This package allows to co-cluster binary
    <doi:10.1016/j.csda.2007.09.007>, contingency <doi:10.1080/03610920903140197>,
    continuous <doi:10.1007/s11634-013-0161-3> and categorical data-sets
    <doi:10.1007/s11222-014-9472-2>. It also provides utility functions to
    visualize the results. This package may be useful for various applications
    in fields of Data mining, Information retrieval, Biology, computer vision
    and many more. More information about the project and comprehensive tutorial
    can be found on the link mentioned in URL.
	"""
	
	homepage = "https://gitlab.inria.fr/iovleff/blockcluster"
	cran = "blockcluster" 

	version("4.5.5", md5="229a6a56d3653a9c8cdbb7837da8a561")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rtkore@1.6.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
