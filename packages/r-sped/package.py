# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSped(RPackage):
	"""Multi-Gene Descent Probabilities

	Do multi-gene descent probabilities
   (Thompson, 1983, <doi:10.1098/rspb.1983.0072>)
   and special cases thereof
   (Thompson, 1986, <doi:10.1002/zoo.1430050210>)
   including inbreeding and kinship coefficients.  But does much more:
   probabilities of any set of genes descending from any other
   set of genes.
	"""
	
	cran = "sped" 

	version("0.3", md5="5d06195cbbbd1054fbb045267d6d6216")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-pooh@0.3:", type=("build", "run"))
