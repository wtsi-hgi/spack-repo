# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlbopictus(RPackage):
	"""Age-Structured Population Dynamics Model

	Implements discrete time deterministic and stochastic age-structured population dynamics models described in Erguler and others (2016) <doi:10.1371/journal.pone.0149282> and Erguler and others (2017) <doi:10.1371/journal.pone.0174293>.
	"""
	
	homepage = "https://github.com/kerguler/albopictusR"
	cran = "albopictus" 

	version("0.5", md5="d0c2cd7889ae7b8d3114d813aebb8605")

