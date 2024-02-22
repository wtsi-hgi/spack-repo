# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptions(RPackage):
	"""Simple, Consistent Package Options

	
    Simple mechanisms for defining and interpreting package options. Provides
    helpers for interpreting environment variables, global options, defining
    default values and more.
	"""
	
	homepage = "https://dgkf.github.io/options/"
	cran = "options" 

	version("0.1.0", md5="911b35d637e46b59a3a1931b2c387098")

