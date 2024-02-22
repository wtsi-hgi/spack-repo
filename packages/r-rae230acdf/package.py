# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230acdf(RPackage):
	"""rae230acdf

	A package containing an environment representing the RAE230A.CDF file.
	"""
	
	bioc = "rae230acdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rae230acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rae230acdf/rae230acdf_2.18.0.tar.gz"]

	version("2.18.0", md5="6f2281124e1be164d5fd599e84f6adbc")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation