# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbmem(RPackage):
	"""Hierarchical Bayesian Analysis of Recognition Memory

	Contains functions for fitting hierarchical versions of
        EVSD, UVSD, DPSD, DPSD with d' restricted to be positive, and
        our gamma signal detection model to recognition memory
        confidence-ratings data.
	"""
	
	homepage = "https://pcn.psychology.msstate.edu/"
	cran = "hbmem" 

	version("0.3-4", md5="4f578a8f7ceacfa12809fa036e280add")

	depends_on("r@1.8:", type=("build", "run"))
