# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniisoregression(RPackage):
	"""Unimodal and Isotonic L1, L2 and Linf Regression

	Perform L1 or L2 isotonic and unimodal regression on 1D weighted or unweighted input vector and isotonic regression on 2D weighted or unweighted input vector. It also performs L infinity isotonic and unimodal regression on 1D unweighted input vector. Reference: Quentin F. Stout (2008) <doi:10.1016/j.csda.2008.08.005>. Spouge, J., Wan, H. & Wilbur, W.(2003) <doi:10.1023/A:1023901806339>. Q.F. Stout (2013) <doi:10.1007/s00453-012-9628-4>.
	"""
	
	homepage = "https://github.com/xzp1995/UniIsoRegression"
	cran = "UniIsoRegression" 

	version("0.0-0", md5="ad72a25985641ecbf4d6df15e44f3296")

	depends_on("r-rcpp", type=("build", "run"))
