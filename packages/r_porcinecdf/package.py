# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPorcinecdf(RPackage):
	"""porcinecdf

	A package containing an environment representing the Porcine.cdf file.
	"""
	
	bioc = "porcinecdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/porcinecdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/porcinecdf/porcinecdf_2.18.0.tar.gz"]

	version("2.18.0", md5="32a60b93829c06a935895fab0a469228")

	depends_on("r-annotationdbi", type=("build", "run"))

