# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvls(RPackage):
	"""The Stark-Parker algorithm for bounded-variable least squares

	An R interface to the Stark-Parker implementation of an
        algorithm for bounded-variable least squares
	"""
	
	cran = "bvls" 

	version("1.4", md5="5f8e2016ecd948926fa163f4873dd4bd")

