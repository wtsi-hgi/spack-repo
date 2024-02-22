# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrea(RPackage):
	"""Bayesian Recurrent Event Analysis

	A function to produce MCMC samples for posterior inference in semiparametric Bayesian discrete time competing risks recurrent events models.
	"""
	
	cran = "brea" 

	version("0.2.0", md5="d84336e843013cee3a02d935461ff408")

