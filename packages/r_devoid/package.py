# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDevoid(RPackage):
	"""A Graphic Device that Does Nothing

	Provides a non-drawing graphic device for benchmarking purpose.
    In order to properly benchmark graphic drawing code it is necessary
    to factor out the device implementation itself so that results are not 
    related to the specific graphics device used during benchmarking. The 
    'devoid' package implements a graphic device that accepts all the required
    calls from R's graphic engine but performs no action. Apart from 
    benchmarking it is unlikely that this device has any practical use.
	"""
	
	homepage = "https://github.com/r-lib/devoid"
	cran = "devoid" 

	version("0.1.2", md5="3705b573a844d7eb88fe0fff6928c4aa")

