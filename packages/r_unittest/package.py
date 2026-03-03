# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnittest(RPackage):
	"""TAP-Compliant Unit Testing

	
    Concise TAP <http://testanything.org/> compliant unit testing package. Authored tests can be run using CMD check with minimal implementation overhead.
	"""
	
	cran = "unittest" 

	version("1.6-1", md5="496dcb241e7a5c77076e96b0365cd8b8")

	depends_on("r@3.6:", type=("build", "run"))
