# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKedd(RPackage):
	"""Kernel Estimator and Bandwidth Selection for Density and Its
Derivatives

	Smoothing techniques and computing bandwidth selectors of the nth derivative of a probability density for one-dimensional data (described in Arsalane Chouaib Guidoum (2020) <arXiv:2012.06102> [stat.CO]).
	"""
	
	homepage = "https://gitlab.com/iagogv/kedd"
	cran = "kedd" 

	version("1.0.4", md5="7c1241e076a55d46bc06dbc3bcdb5eb0")

	depends_on("r@2.15:", type=("build", "run"))
