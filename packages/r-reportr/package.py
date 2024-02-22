# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReportr(RPackage):
	"""A General Message and Error Reporting System

	Provides a system for reporting messages, which provides certain useful features over the standard R system, such as the incorporation of output consolidation, message filtering, assertions, expression substitution, automatic generation of stack traces for debugging, and conditional reporting based on the current "output level".
	"""
	
	homepage = "https://github.com/jonclayden/reportr"
	cran = "reportr" 

	version("1.3.0", md5="3c6c8d1d2d67492808f1c6327c20e109")

	depends_on("r-ore", type=("build", "run"))
