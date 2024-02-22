# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu19ksubacdf(RPackage):
	"""mu19ksubacdf

	A package containing an environment representing the Mu19KsubA.CDF file.
	"""
	
	bioc = "mu19ksubacdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mu19ksubacdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mu19ksubacdf/mu19ksubacdf_2.18.0.tar.gz"]

	version("2.18.0", md5="83a9e7a3bac665b655786e66dbd77848")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation