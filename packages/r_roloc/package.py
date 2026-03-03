# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoloc(RPackage):
	"""Convert Colour Specification to Colour Name

	Functions to convert an R colour specification to a colour name. The user can select and create different lists of colour names and different colour metrics for the conversion.
	"""
	
	cran = "roloc" 

	version("0.1-2", md5="0b8030e133f702452aa250c83caeaf97")

	depends_on("r-colorspace", type=("build", "run"))
