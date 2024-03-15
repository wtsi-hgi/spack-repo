# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrcovhd(RPackage):
	"""Robust Multivariate Methods for High Dimensional Data

	Robust multivariate methods for high dimensional data including
        outlier detection (Filzmoser and Todorov (2013) <doi:10.1016/j.ins.2012.10.017>), 
        robust sparse PCA (Croux et al. (2013) <doi:10.1080/00401706.2012.727746>, Todorov and Filzmoser (2013) <doi:10.1007/978-3-642-33042-1_31>), 
        robust PLS (Todorov and Filzmoser (2014) <doi:10.17713/ajs.v43i4.44>), 
        and robust sparse classification (Ortner et al. (2020) <doi:10.1007/s10618-019-00666-8>).
	"""
	
	homepage = "https://github.com/valentint/rrcovHD"
	cran = "rrcovHD" 

	version("0.3-0", md5="51f51bfe672d2369076379401ed90810")

	depends_on("r-rrcov@1.3.7:", type=("build", "run"))
	depends_on("r-robustbase@0.92.1:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-spls", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-robusthd", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
