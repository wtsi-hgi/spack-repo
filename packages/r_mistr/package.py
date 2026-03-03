# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMistr(RPackage):
	"""Mixture and Composite Distributions

	A flexible computational framework for mixture distributions with the focus on the composite models.
	"""
	
	cran = "mistr" 

	version("0.0.6", md5="6eb5901c5cc3986266f42a9a28d90f62")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
