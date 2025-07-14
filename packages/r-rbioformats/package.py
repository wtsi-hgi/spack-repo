# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbioformats(RPackage):
	"""R interface to Bio-Formats

	An R package which interfaces the OME Bio-Formats Java library to allow reading of proprietary microscopy image data and metadata.
	"""
	
	homepage = "https://github.com/aoles/RBioFormats"
	bioc = "RBioFormats"

	version("1.8.0", commit="572dde8042e9aae2159a34b04e41cfd90201ca4a")
	version("1.2.0", commit="85f35c53616eb7647be16b26fd8235bd596820bf")

	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-rjava@0.9.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
