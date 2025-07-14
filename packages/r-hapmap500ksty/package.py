# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap500ksty(RPackage):
	"""Sample data - Hapmap 500K STY Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmap500ksty" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hapmap500ksty_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hapmap500ksty/hapmap500ksty_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="f95871dad86e454d3e2fd5ebbe6a674a0f9fa163273feb82a8b75afbc4dc233c")


