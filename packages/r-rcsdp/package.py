# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcsdp(RPackage):
	"""R Interface to the CSDP Semidefinite Programming Library

	R interface to the CSDP semidefinite programming library. Installs version 6.1.1 of CSDP from the COIN-OR website if required. An existing installation of CSDP may be used by passing the proper configure arguments to the installation command. See the INSTALL file for further details.
	"""
	
	homepage = "https://github.com/coin-or/Csdp/"
	cran = "Rcsdp" 

	version("0.1.57.5", md5="dec4357fda5865cfabd9f4ad7bf74d76")

