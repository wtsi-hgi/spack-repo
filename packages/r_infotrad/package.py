# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfotrad(RPackage):
	"""Calculates the Probability of Informed Trading (PIN)

	Estimates the probability of informed trading (PIN) initially introduced by Easley et. al. (1996) <doi:10.1111/j.1540-6261.1996.tb04074.x> . Contribution of the package is that it uses likelihood factorizations of Easley et. al. (2010) <doi:10.1017/S0022109010000074> (EHO factorization) and Lin and Ke (2011) <doi:10.1016/j.finmar.2011.03.001> (LK factorization). Moreover, the package uses different estimation algorithms. Specifically, the grid-search algorithm proposed by Yan and Zhang (2012) <doi:10.1016/j.jbankfin.2011.08.003> , hierarchical agglomerative clustering approach proposed by Gan et. al. (2015) <doi:10.1080/14697688.2015.1023336> and later extended by Ersan and Alici (2016) <doi:10.1016/j.intfin.2016.04.001> .
	"""
	
	cran = "InfoTrad" 

	version("1.2", md5="be8df0c3e92418004fbba82553dc10c1")

	depends_on("r-nloptr", type=("build", "run"))
