# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImport(RPackage):
	"""An Import Mechanism for R

	Alternative mechanism for importing objects from packages
    and R modules. The syntax allows for importing multiple objects with a single
    command in an expressive way. The import package bridges some of the gap
    between using library (or require) and direct (single-object) imports.
    Furthermore the imported objects are not placed in the current environment.
	"""
	
	homepage = "https://github.com/rticulate/import"
	cran = "import" 

	version("1.3.2", md5="06cc0f3641fe73d37fef3bfd651d2443")

