# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROperators(RPackage):
	"""Additional Binary Operators

	A set of binary operators for common tasks such as regex
        manipulation.
	"""
	
	homepage = "https://github.com/romainfrancois/operators"
	cran = "operators" 

	version("0.1-8", md5="50c905bae88834362eff7dcbabd3cb94")

	depends_on("r@3.1:", type=("build", "run"))
