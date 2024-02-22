# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddscales(RPackage):
	"""Adds Labeled Center Line and Scale Lines/Regions to Trellis
Plots

	Modifies trellis objects by adding horizontal and/or vertical
 reference lines or shaded regions that provide visual scaling information. 
 This is mostly useful in multi-panel plots that use the relation = 'free'
 option in their 'scales' argument list.
	"""
	
	cran = "addScales" 

	version("1.0-1", md5="07a3238fa525521795a25d2b2b8cdcb1")

	depends_on("r-lattice@0.20.38:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
