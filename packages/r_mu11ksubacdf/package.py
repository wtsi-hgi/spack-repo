# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu11ksubacdf(RPackage):
	"""mu11ksubacdf

	A package containing an environment representing the Mu11KsubA.CDF file.
	"""
	
	bioc = "mu11ksubacdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu11ksubacdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu11ksubacdf/mu11ksubacdf_2.18.0.tar.gz"]

	version("2.18.0", md5="52fb8ac56435775022fb62f40efafd22")

	depends_on("r-annotationdbi", type=("build", "run"))

