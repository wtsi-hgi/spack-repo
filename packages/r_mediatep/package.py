# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMediatep(RPackage):
	"""Mediation Analysis Based on the Product Method

	Functions for calculating the point and interval estimates of the natural indirect effect (NIE), total effect (TE), and mediation proportion (MP), based on the product approach. We perform the methods considered in Cheng, Spiegelman, and Li (2021) Estimating the natural indirect effect and the mediation proportion via the product method.
	"""
	
	cran = "mediateP" 

	version("0.2.0", md5="d4da84cd10ad7ae38377c1cd44d890a8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
