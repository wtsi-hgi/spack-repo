# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlpoisson(RPackage):
	"""Prediction Limits for Poisson Distribution

	Prediction limits for the Poisson distribution
  are produced from both frequentist and Bayesian viewpoints. Limiting results
  are provided in a Bayesian setting with uniform, Jeffreys and gamma as prior
  distributions. More details on the methodology are discussed in Bejleri and
  Nandram (2018) <doi:10.1080/03610926.2017.1373814> and Bejleri, Sartore and
  Nandram (2021) <doi:10.1007/s42952-021-00157-x>.
	"""
	
	cran = "plpoisson" 

	version("0.3.0", md5="f6072a23f17626c37971fbe23dccf5c6")

