# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLanguageserversetup(RPackage):
	"""Automated Setup and Auto Run for R Language Server

	Allows to install the R 'languageserver' with all dependencies
    into a separate library and use that independent installation
    automatically when R is instantiated as a language server process.
    Useful for making language server seamless to use without
    running into package version conflicts.
	"""
	
	homepage = "https://github.com/jozefhajnala/languageserversetup"
	cran = "languageserversetup" 

	version("0.1.2", md5="73b597c0bcea57cb883456fff11c921f")

