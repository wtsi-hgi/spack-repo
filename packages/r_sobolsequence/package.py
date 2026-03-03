# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSobolsequence(RPackage):
	"""Sobol Sequences with Better Two-Dimensional Projections

	R implementation of S. Joe and F. Y. Kuo(2008)
        <DOI:10.1137/070709359>.
        The implementation is based on the data file new-joe-kuo-6.21201
        <http://web.maths.unsw.edu.au/~fkuo/sobol/>.
	"""
	
	homepage = "http://web.maths.unsw.edu.au/~fkuo/sobol/"
	cran = "SobolSequence" 

	version("1.0", md5="6dd9ff3a3778ecf86d5a7e24164ef26c")

	depends_on("r-rcpp", type=("build", "run"))
