# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrto(RPackage):
	"""Tools for the Analysis of Gutenberg-Richter Distributions of
Earthquake Magnitudes

	Offers functions for the comparison of Gutenberg-Richter 
	b-values. Several functions in GRTo are helpful for the assessment of the
	quality of seismicity catalogs. 
	"""
	
	cran = "GRTo" 

	version("1.3", md5="8ef4eec5fb1e98d6549e418545d9ed33")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
