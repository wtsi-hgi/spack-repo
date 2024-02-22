# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeroLero(RPackage):
	"""Generate 'Lero Lero' Quotes

	Generates quotes from 'Lero Lero', a database for meaningless sentences filled with corporate buzzwords, intended to be used as corporate lorem ipsum (see <http://www.lerolero.com/> for more information). Unfortunately, quotes are currently portuguese-only.
	"""
	
	cran = "lero.lero" 

	version("0.2", md5="122700702e30ba3e453be947a07c96cb")

