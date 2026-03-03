# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimbleapt(RPackage):
	"""Adaptive Parallel Tempering for 'NIMBLE'

	Functions for adaptive parallel tempering (APT) with NIMBLE models. Adapted from 'Lacki' & 'Miasojedow' (2016) <DOI:10.1007/s11222-015-9579-0> and 'Miasojedow, Moulines and Vihola' (2013) <DOI:10.1080/10618600.2013.778779>.
	"""
	
	homepage = "https://github.com/DRJP/nimbleAPT"
	cran = "nimbleAPT" 

	version("1.0.4", md5="a4905a961816db93fc36fa8016f890df")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-nimble", type=("build", "run"))
