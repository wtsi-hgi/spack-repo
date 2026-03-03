# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaper(RPackage):
	"""A Toolbox for Writing Pretty Papers and Reports

	A toolbox for writing 'knitr', 'Sweave' or other 'LaTeX'- or 'markdown'-based
	     reports and to prettify the output of various estimated models.
	"""
	
	homepage = "https://github.com/hofnerb/papeR"
	cran = "papeR" 

	version("1.0-5", md5="480894c8a28a44dcf5f04983318bad11")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
