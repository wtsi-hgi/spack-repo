# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesignParameters(RPackage):
	"""Parameters of the Experimental Designs

	Here, a function has been developed to generate parameters of the input designs, as well as incidence matrices. This is a general function that can be used to investigate the characterization properties of any block design.
	"""
	
	cran = "Design.parameters" 

	version("0.1.0", md5="8956e4949213175b642f864c0bbb825a")

