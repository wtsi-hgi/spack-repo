# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdaconcur(RPackage):
	"""Concurrent Regression and History Index Models for Functional
Data

	Provides an implementation of concurrent or varying coefficient regression methods for 
    functional data. The implementations are done for both dense and sparsely observed functional
    data. Pointwise confidence bands can be constructed for each case. Further, the influence of
    past predictor values are modeled by a smooth history index function, 
    while the effects on the response are described by smooth varying coefficient functions, 
    which are very useful in analyzing real data such as COVID data.
    References: Yao, F., Müller, H.G., Wang, J.L. (2005) <doi: 10.1214/009053605000000660>.
                Sentürk, D., Müller, H.G. (2010) <doi: 10.1198/jasa.2010.tm09228>.
	"""
	
	homepage = "https://github.com/functionaldata/tFDAconcur"
	cran = "fdaconcur" 

	version("0.1.2", md5="302f1b739da039c4fa08f86bc73d90c8")

	depends_on("r-fdapace", type=("build", "run"))
