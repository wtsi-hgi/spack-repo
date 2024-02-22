# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObmbpkg(RPackage):
	"""Estimate the Population Size for the Mb Capture-Recapture Model

	Applies an objective Bayesian method to the Mb capture-recapture model to estimate the population size N.  The Mb model is a class of capture-recapture methods used to account for variations in capture probability due to animal behavior.  Under the Mb formulation,  the initial capture of an animal may effect the probability of subsequent captures due to their becoming "trap happy" or "trap shy."
	"""
	
	cran = "OBMbpkg" 

	version("1.0.0", md5="13a835808ccea8da59ab9aafac083e62")

