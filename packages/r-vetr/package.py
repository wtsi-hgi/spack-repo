# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVetr(RPackage):
	"""Trust, but Verify

	Declarative template-based framework for verifying that objects
  meet structural requirements, and auto-composing error messages when they do
  not.
	"""
	
	homepage = "https://github.com/brodieG/vetr"
	cran = "vetr" 

	version("0.2.16", md5="61351bc9cdb7932baac9bf8bf3002a85")

	depends_on("r@3.2:", type=("build", "run"))
