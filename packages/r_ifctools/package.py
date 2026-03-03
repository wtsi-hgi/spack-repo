# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfctools(RPackage):
	"""Italian Fiscal Code ('Codice Fiscale') Utilities

	Provides utility functions to deal with Italian fiscal
    code ('codice fiscale').
	"""
	
	homepage = "https://github.com/lbraglia/ifctools"
	cran = "ifctools" 

	version("0.3.6", md5="b38078c1ca57e05356eecefa62c20330")

	depends_on("r@3.1.1:", type=("build", "run"))
