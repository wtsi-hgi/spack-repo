# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrand(RPackage):
	"""Guidelines for Reporting About Network Data

	Interactively applies the Guidelines for Reporting About Network Data (GRAND) to an 'igraph' object, and generates a uniform narrative or tabular description of the object.
	"""
	
	homepage = "https://github.com/zpneal/grand"
	cran = "grand" 

	version("0.9.0", md5="8f0572ae94767154a97379ffdbdc00ed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
