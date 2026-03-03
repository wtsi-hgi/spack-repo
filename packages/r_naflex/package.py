# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaflex(RPackage):
	"""Flexible Options for Handling Missing Values

	For use in summary functions to omit missing values 
    conditionally using specified checks.
	"""
	
	homepage = "https://github.com/dannyparsons/naflex"
	cran = "naflex" 

	version("0.1.0", md5="f764073148e50bebc654372c74a13f8a")

