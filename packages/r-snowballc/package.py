# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnowballc(RPackage):
	"""Snowball Stemmers Based on the C 'libstemmer' UTF-8 Library

	An R interface to the C 'libstemmer' library that implements
  Porter's word stemming algorithm for collapsing words to a common
  root to aid comparison of vocabulary. Currently supported languages are
  Arabic, Basque, Catalan, Danish, Dutch, English, Finnish, French, German, Greek,
  Hindi, Hungarian, Indonesian, Irish, Italian, Lithuanian, Nepali,
  Norwegian, Portuguese, Romanian, Russian, Spanish, Swedish, Tamil
  and Turkish.
	"""
	
	homepage = "https://github.com/nalimilan/R.TeMiS"
	cran = "SnowballC" 

	version("0.7.1", md5="c95c904382d30d7256d1fa710f9327f0")

