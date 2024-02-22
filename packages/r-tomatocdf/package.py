# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTomatocdf(RPackage):
	"""tomatocdf

	A package containing an environment representing the Tomato.cdf file.
	"""
	
	bioc = "tomatocdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/tomatocdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/tomatocdf/tomatocdf_2.18.0.tar.gz"]

	version("2.18.0", md5="200efc0637788d4bd3263fc9183c1aa6")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation