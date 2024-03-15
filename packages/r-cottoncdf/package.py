# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCottoncdf(RPackage):
	"""cottoncdf

	A package containing an environment representing the Cotton.cdf file.
	"""
	
	bioc = "cottoncdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/cottoncdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/cottoncdf/cottoncdf_2.18.0.tar.gz"]

	version("2.18.0", md5="b9d2a4b43235c6e531b78cca006e84b2")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation