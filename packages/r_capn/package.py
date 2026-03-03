# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCapn(RPackage):
	"""Capital Asset Pricing for Nature

	Implements approximation methods for natural capital asset prices suggested by Fenichel and Abbott (2014) <doi:10.1086/676034> in Journal of the Associations of Environmental and Resource Economists (JAERE), Fenichel et al. (2016) <doi:10.1073/pnas.1513779113> in Proceedings of the National Academy of Sciences (PNAS), and Yun et al. (2017) in PNAS (accepted), and their extensions: creating Chebyshev polynomial nodes and grids, calculating basis of Chebyshev polynomials, approximation and their simulations for: V-approximation (single and multiple stocks, PNAS), P-approximation (single stock, PNAS), and Pdot-approximation (single stock, JAERE). Development of this package was generously supported by the Knobloch Family Foundation.
	"""
	
	cran = "capn" 

	version("1.0.0", md5="4da62506d32de1f68d94a150e41e07a7")

	depends_on("r@3.0.1:", type=("build", "run"))
