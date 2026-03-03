# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpressionistColors(RPackage):
	"""Impressionism's Color Palettes

	Provides color palettes from Impressionism and post-Impressionism artworks. This package allows to select colors combinations while looking at the original paintings where colors were sampled from.
	"""
	
	cran = "impressionist.colors" 

	version("1.0", md5="6077aff82e7f5d84f171580b7a1926ae")

	depends_on("r@2.10:", type=("build", "run"))
