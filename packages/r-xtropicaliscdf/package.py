# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtropicaliscdf(RPackage):
	"""xtropicaliscdf

	A package containing an environment representing the X_tropicalis.cdf file.
	"""
	
	bioc = "xtropicaliscdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/xtropicaliscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/xtropicaliscdf/xtropicaliscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="253e3cde76a393789e124f395820e947")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation