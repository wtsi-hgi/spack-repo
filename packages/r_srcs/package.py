# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrcs(RPackage):
	"""Statistical Ranking Color Scheme for Multiple Pairwise
Comparisons

	Implementation of the SRCS method for a color-based visualization of the
    results of multiple pairwise tests on a large number of problem configurations, proposed in: 
    I.G. del Amo, D.A. Pelta. SRCS: a technique for comparing multiple algorithms under several
    factors in dynamic optimization problems. In: E. Alba, A. Nakib, P. Siarry
    (Eds.), Metaheuristics for Dynamic Optimization. Series: Studies in
    Computational Intelligence 433, Springer, Berlin/Heidelberg, 2012.
	"""
	
	homepage = "http://decsai.ugr.es/~pjvi/r-packages.html"
	cran = "SRCS" 

	version("1.1", md5="835234b194799eeab017888d5004fd27")

