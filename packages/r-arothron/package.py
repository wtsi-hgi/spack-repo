# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArothron(RPackage):
	"""Geometric Morphometric Methods and Virtual Anthropology Tools

	Tools for geometric morphometric analysis. The package includes tools of virtual anthropology to align two not articulated parts belonging to the same specimen, to build virtual cavities as endocast (Profico et al, 2021 <doi:10.1002/ajpa.24340>).
	"""
	
	cran = "Arothron" 

	version("2.0.5", md5="8c35dc41e4cb691ed08ca76b90ba5fe4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind@1.4:", type=("build", "run"))
	depends_on("r-alphashape3d@1.3:", type=("build", "run"))
	depends_on("r-compositions@1.40.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-geometry@0.3.6:", type=("build", "run"))
	depends_on("r-morpho@2.5:", type=("build", "run"))
	depends_on("r-rgl@1.0.1:", type=("build", "run"))
	depends_on("r-rvcg@0.17:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-vegan@2.4:", type=("build", "run"))
