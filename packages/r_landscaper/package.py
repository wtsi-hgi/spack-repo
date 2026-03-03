# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandscaper(RPackage):
	"""Categorical Landscape Simulation Facility

	Simulates categorical maps on actual geographical realms, starting from either empty landscapes or landscapes provided by the user (e.g. land use maps). Allows to tweak or create landscapes while retaining a high degree of control on its features, without the hassle of specifying each location attribute. In this it differs from other tools which generate null or neutral landscapes in a theoretical space. The basic algorithm currently implemented uses a simple agent style/cellular automata growth model, with no rules (apart from areas of exclusion) and von Neumann neighbourhood (four cells, aka Rook case). Outputs are raster dataset exportable to any common GIS format.
	"""
	
	homepage = "https://github.com/dariomasante/landscapeR"
	cran = "landscapeR" 

	version("1.2", md5="9daa79c2fc4335bf603395a36dd5dc87")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
