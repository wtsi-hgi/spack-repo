# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChnosz(RPackage):
	"""Thermodynamic Calculations and Diagrams for Geochemistry

	An integrated set of tools for thermodynamic calculations in
  aqueous geochemistry and geobiochemistry. Functions are provided for writing
  balanced reactions to form species from user-selected basis species and for
  calculating the standard molal properties of species and reactions, including
  the standard Gibbs energy and equilibrium constant. Calculations of the
  non-equilibrium chemical affinity and equilibrium chemical activity of species
  can be portrayed on diagrams as a function of temperature, pressure, or
  activity of basis species; in two dimensions, this gives a maximum affinity or
  predominance diagram. The diagrams have formatted chemical formulas and axis
  labels, and water stability limits can be added to Eh-pH, oxygen fugacity-
  temperature, and other diagrams with a redox variable. The package has been
  developed to handle common calculations in aqueous geochemistry, such as
  solubility due to complexation of metal ions, mineral buffers of redox or pH,
  and changing the basis species across a diagram ("mosaic diagrams"). CHNOSZ
  also implements a group additivity algorithm for the standard thermodynamic
  properties of proteins.
	"""
	
	homepage = "https://www.chnosz.net/"
	cran = "CHNOSZ" 

	version("2.1.0", md5="00d2ed5999c047c546132ce4c9e87909")

	depends_on("r@3.1:", type=("build", "run"))
