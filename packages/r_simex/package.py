# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimex(RPackage):
	"""SIMEX- And MCSIMEX-Algorithm for Measurement Error Models

	Implementation of the SIMEX-Algorithm by Cook & Stefanski (1994) <doi:10.1080/01621459.1994.10476871> and
    MCSIMEX by Küchenhoff, Mwalili & Lesaffre (2006) <doi:10.1111/j.1541-0420.2005.00396.x>.
	"""
	
	homepage = "http://wolfganglederer.github.io/simex/"
	cran = "simex" 

	version("1.8", md5="04b100a1b422e5a25398c117573b2e9f")

