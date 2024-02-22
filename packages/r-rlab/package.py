# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlab(RPackage):
	"""Functions and Datasets Required for ST370 Class

	Provides functions and datasets required for the ST 370 course at North Carolina State University.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "Rlab" 

	version("4.0", md5="37be3a8dbc0898ecd033f160c0123eb7")

	depends_on("r@2.10:", type=("build", "run"))
