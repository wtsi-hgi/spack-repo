# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaninecdf(RPackage):
	"""caninecdf

	A package containing an environment representing the Canine.cdf file.
	"""
	
	bioc = "caninecdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/caninecdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/caninecdf/caninecdf_2.18.0.tar.gz"]

	version("2.18.0", md5="656f845cc66890015a4e13c5304ec262")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation