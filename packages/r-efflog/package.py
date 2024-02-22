# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfflog(RPackage):
	"""The Causal Effects for a Causal Loglinear Model

	Fitting a causal loglinear model and calculating the causal effects for a causal loglinear model with the multiplicative interaction or without the multiplicative interaction, obtaining the natural direct, indirect and the total effect. It calculates also the cell effect, which is a new interaction effect.
	"""
	
	cran = "efflog" 

	version("1.0", md5="05bf8d579f2bbbbdb3ca0c1ccaca87ed")

	depends_on("r@2.10.1:", type=("build", "run"))
