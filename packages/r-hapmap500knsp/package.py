# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap500knsp(RPackage):
	"""Sample data - Hapmap 500K NSP Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmap500knsp" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hapmap500knsp_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hapmap500knsp/hapmap500knsp_1.44.0.tar.gz"]

	version("1.44.0", sha256="d440952bced1ac84f10eac500e4ce095b6e0c663baa86c76627e9a0d113c8ace")


