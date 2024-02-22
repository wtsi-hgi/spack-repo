# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVtable(RPackage):
	"""Variable Table for Variable Documentation

	Automatically generates HTML variable documentation including variable names, labels, classes, value labels (if applicable), value ranges, and summary statistics. See the vignette "vtable" for a package overview.
	"""
	
	homepage = "https://nickch-k.github.io/vtable/"
	cran = "vtable" 

	version("1.4.6", md5="e66482cb725aa70e8df3067a5a8161d3")

	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
