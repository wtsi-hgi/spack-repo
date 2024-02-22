# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactr(RPackage):
	"""React Helpers

	Make it easy to use 'React' in R with 'htmlwidget' scaffolds,
              helper dependency functions, an embedded 'Babel' 'transpiler',
              and examples.
	"""
	
	homepage = "https://github.com/react-R/reactR"
	cran = "reactR" 

	version("0.5.0", md5="09167beb9eb045a977a1518f99c688b8")

	depends_on("r-htmltools", type=("build", "run"))
