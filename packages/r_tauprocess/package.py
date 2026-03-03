# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTauprocess(RPackage):
	"""Tau Measure with Right-Censored Data

	A clinically meaningful measures of treatment effects for right-censored data 
  are provided, based on the concept of Kendall's tau, along with the corresponding inference procedures.
  Two plots of tau processes, with the option to account for the cure fraction or not, are available.
  The plots of tau processes serve as useful graphical tools for monitoring the relative performances over time. 
	"""
	
	homepage = "https://github.com/s07308/tauProcess"
	cran = "tauProcess" 

	version("2.1.3", md5="4f743cc8b85fe6864971c4ff9dbf7456")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
