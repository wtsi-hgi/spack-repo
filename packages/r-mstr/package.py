# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstr(RPackage):
	"""Procedures to Generate Patterns under Multistage Testing

	Generation of response patterns under dichotomous and polytomous computerized multistage testing (MST) framework. It holds various item response theory (IRT) and score-based methods to select the next module and estimate ability levels (Magis, Yan and von Davier (2017, ISBN:978-3-319-69218-0)). 
	"""
	
	cran = "mstR" 

	version("1.2", md5="d23bc21179b614dfcc5e7113e24aabba")

	depends_on("r@2.8:", type=("build", "run"))
