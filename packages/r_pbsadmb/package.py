# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbsadmb(RPackage):
	"""ADMB for R Using Scripts or GUI

	A collection of software provides R support for 'ADMB'
             (Automatic Differentiation Model Builder) and a 'GUI'
             interface facilitates the conversion of 'ADMB' template
             code to 'C code' followed by compilation to a binary executable.
             Stand-alone functions can also be run by users
             not interested in clicking a 'GUI'.
	"""
	
	homepage = "https://github.com/pbs-software/pbs-admb"
	cran = "PBSadmb" 

	version("1.1.6", md5="03cf89ab459061d040e83b5cf4e78b3c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pbsmodelling@2.68.6:", type=("build", "run"))
