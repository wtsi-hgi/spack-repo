# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoopsd(RPackage):
	"""R Object Oriented Programming for Statistical Distribution

	Statistical distribution in OOP (Object Oriented Programming) way.
             This package proposes a R6 class interface to classic statistical
             distribution, and new distributions can be easily added with the
             class AbstractDist. A useful point is the generic fit() method for
             each class, which uses a maximum likelihood estimation to find the
             parameters of a dataset, see, e.g. Hastie, T. and al (2009)
             <isbn:978-0-387-84857-0>. Furthermore, the rv_histogram class
             gives a non-parametric fit, with the same accessors that for the
             classic distribution. Finally, three random generators useful to
             build synthetic data are given: a multivariate normal generator, an
             orthogonal matrix generator, and a symmetric positive definite
             matrix generator, see Mezzadri, F. (2007)
             <arXiv:math-ph/0609050>.
	"""
	
	homepage = "https://github.com/yrobink/ROOPSD"
	cran = "ROOPSD" 

	version("0.3.9", md5="4b117b429b56b8a579004c828e6f7078")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lmoments", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
