# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQfrm(RPackage):
	"""Pricing of Vanilla and Exotic Option Contracts

	
  Option pricing (financial derivatives) techniques mainly following textbook 'Options, Futures and Other Derivatives', 9ed by John C.Hull, 2014. Prentice Hall. Implementations are via binomial tree option model (BOPM), Black-Scholes model, Monte Carlo simulations, etc. 
  This package is a result of Quantitative Financial Risk Management course (STAT 449 and STAT 649) at Rice University, Houston, TX, USA, taught by Oleg Melnikov, statistics PhD student, as of Spring 2015.
	"""
	
	homepage = "http://Oleg.Rice.edu"
	cran = "QFRM" 

	version("1.0.1", md5="657673b855f0f56ee6b8faafe92d7efb")

	depends_on("r@2.14:", type=("build", "run"))
