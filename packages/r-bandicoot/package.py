# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBandicoot(RPackage):
	"""Light-Weight 'python'-Like Object-Oriented System

	A light-weight object-oriented system with 'python'-like syntax which supports multiple inheritances and incorporates a 'python'-like method resolution order.
	"""
	
	homepage = "https://tengmcing.github.io/bandicoot/"
	cran = "bandicoot" 

	version("1.0.0", md5="422075b1cb996c35a769791be2050914")

	depends_on("r-cli", type=("build", "run"))
