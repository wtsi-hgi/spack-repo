# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGepaf(RPackage):
	"""Google Encoded Polyline Algorithm Format

	Encode and decode the Google Encoded Polyline Algorithm Format (<https://developers.google.com/maps/documentation/utilities/polylinealgorithm>).
	"""
	
	homepage = "https://github.com/mthh/gepaf"
	cran = "gepaf" 

	version("0.1.1", md5="405cf7f424a9eb99060cfdccb1ae0ae9")

	depends_on("r-bitops", type=("build", "run"))
