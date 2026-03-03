# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGps(RPackage):
	"""General P-Splines

	General P-splines are non-uniform B-splines penalized by a general difference penalty, proposed by Li and Cao (2022) <arXiv:2201.06808>. Constructible on arbitrary knots, they extend the standard P-splines of Eilers and Marx (1996) <doi:10.1214/ss/1038425655>. They are also related to the O-splines of O'Sullivan (1986) <doi:10.1214/ss/1177013525> via a sandwich formula that links a general difference penalty to a derivative penalty. The package includes routines for setting up and handling difference and derivative penalties. It also fits P-splines and O-splines to (x, y) data (optionally weighted) for a grid of smoothing parameter values in the automatic search intervals of Li and Cao (2023) <doi:10.1007/s11222-022-10178-z>. It aims to facilitate other packages to implement P-splines or O-splines as a smoothing tool in their model estimation framework.
	"""
	
	homepage = "https://github.com/ZheyuanLi/gps"
	cran = "gps" 

	version("1.2", md5="f2e0ddf0875e2540928a89214b6d05fd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
