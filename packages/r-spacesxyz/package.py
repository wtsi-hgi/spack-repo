# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacesxyz(RPackage):
	"""CIE XYZ and some of Its Derived Color Spaces

	Functions for converting among CIE XYZ, xyY, Lab, and Luv.
      Calculate Correlated Color Temperature (CCT) and the Planckian and daylight loci.  
      The XYZs of some standard illuminants and some standard linear chromatic adaptation transforms (CATs) are included.
      Three standard color difference metrics are included.
	"""
	
	cran = "spacesXYZ" 

	version("1.3-0", md5="cb60cc6e2ed587cd9b31a58658734524")

	depends_on("r@3.2:", type=("build", "run"))
