# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatex(RPackage):
	"""Heat exchange calculations during physical activity

	The heatex package calculates heat storage in the body and
        the components of heat exchange (conductive, convective,
        radiative, and evaporative) between the body and the
        environment during physical activity based on the principles of
        partitional calorimetry. The program enables heat exchange
        calculations for a range of environmental conditions when
        wearing various clothing ensembles.
	"""
	
	cran = "heatex" 

	version("1.0", md5="cee9eb3173af1dd48284d428bacb526d")

