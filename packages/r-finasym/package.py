# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinasym(RPackage):
	"""Classifies implicit trading activity from market quotes and
computes the probability of informed trading

	This package accomplishes two tasks: a) it classifies
        implicit trading activity from quotes in OTC markets using the
        algorithm of Lee and Ready (1991); b) based on information for
        trade initiation, the package computes the probability of
        informed trading of Easley and O'Hara (1987).
	"""
	
	cran = "FinAsym" 

	version("1.0", md5="67a27d2bd10bf4dc59d63d88aa09351e")

