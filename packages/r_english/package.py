# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnglish(RPackage):
	"""Translate Integers into English

	Allow numbers to be presented in an English language
        version, one, two, three, ...  Ordinals are also available,
        first, second, third, ... and indefinite article choice, "a" or "an".
	"""
	
	cran = "english" 

	version("1.2-6", md5="1215268b9fabf76a6e2c7c150af7e6d8")

