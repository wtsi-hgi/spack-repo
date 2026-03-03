# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRound(RPackage):
	"""Rounding to Decimal Digits

	Decimal rounding is non-trivial in binary arithmetic.  ISO
  standard round to even is more rare than typically assumed as most decimal fractions
  are not exactly representable in binary.  Our 'roundX()' versions explore differences
  between current and potential future versions of round() in R.
  Further, provides (some partly related) C99 math lib functions not in base R.
	"""
	
	homepage = "https://gitlab.com/mmaechler/round/"
	cran = "round" 

	version("0.21-0.2", md5="44d20a299505ec805239991d860dcb44")

