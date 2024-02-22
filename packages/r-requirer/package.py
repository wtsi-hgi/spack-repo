# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRequirer(RPackage):
	"""R Source Code Modularizer

	Modularizes source code. Keeps the global environment clean,
    explicifies interdependencies. Inspired by 'RequireJS'<http://requirejs.org/>.
	"""
	
	cran = "requireR" 

	version("1.0.0.1", md5="58bb4d89472c864e72b8330c8ab09017")

	depends_on("r@3.3.1:", type=("build", "run"))
