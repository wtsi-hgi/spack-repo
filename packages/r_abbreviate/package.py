# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbbreviate(RPackage):
	"""Readable String Abbreviation

	Strings are abbreviated to at least "minlength" characters, such that they remain unique 
    (if they were). The abbreviations should be recognisable.
	"""
	
	homepage = "https://github.com/sigbertklinke/abbreviate"
	cran = "abbreviate" 

	version("0.1", md5="37285eddefb6b0fce95783bf21b32999")

