# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterfaceqpcr(RPackage):
	"""GUI to Analyse qPCR Results after PMA Treatment or not

	Graphical User Interface allowing to determine the concentration in the sample in CFU per mL or in number of copies per mL provided to qPCR results after with or without PMA treatment. This package is simply to use because no knowledge in R commands is necessary. A graphic represents the standard curve, and a table containing the result for each sample is created.
	"""
	
	cran = "InterfaceqPCR" 

	version("1.0.1", md5="62e7e7b364790d4854f13c426576ff8a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
