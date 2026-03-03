# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThankr(RPackage):
	"""Find Out Who Maintains the Packages you Use

	Find out who maintains the packages you use in
             your current session or in your package library and
             maybe say 'thank you'.
	"""
	
	cran = "thankr" 

	version("1.0.0", md5="c3b0639c9db5e1a49ae2a3b54461d271")

