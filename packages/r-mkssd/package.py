# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkssd(RPackage):
	"""Efficient Multi-Level k-Circulant Supersaturated Designs

	Generates efficient balanced non-aliased multi-level k-circulant supersaturated designs by interchanging the elements of the generator vector. Attempts to generate a supersaturated design that has chisquare efficiency more than user specified efficiency level (mef). Displays the progress of generation of an efficient multi-level k-circulant design through a progress bar. The progress of 100% means that one full round of interchange is completed. More than one full round (typically 4-5 rounds) of interchange may be required for larger designs. 
	"""
	
	cran = "mkssd" 

	version("1.2", md5="57a7119c88dd75f24fc86f00281cd00c")

	depends_on("r@2.13:", type=("build", "run"))
