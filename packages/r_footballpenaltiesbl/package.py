# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFootballpenaltiesbl(RPackage):
	"""Penalties in the German Men's Football Bundesliga

	Basic analysis of all penalties taken in the German men's Bundesliga
  between the start of its inaugural season and May 2017. The main functions are
  suitable printing and plotting functions. Flexible selection of a player is
  supported via grep. Missed penalties can easily be included or excluded, depending
  on the user's wishes.
	"""
	
	cran = "footballpenaltiesBL" 

	version("1.0.0", md5="6a2d32855c811f4dedd075076f50a47f")

	depends_on("r@4:", type=("build", "run"))
