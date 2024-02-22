# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNugomm1a520177cdf(RPackage):
	"""nugomm1a520177cdf

	A package containing an environment representing the NuGO_Mm1a520177.cdf file.
	"""
	
	bioc = "nugomm1a520177cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/nugomm1a520177cdf_3.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/nugomm1a520177cdf/nugomm1a520177cdf_3.4.0.tar.gz"]

	version("3.4.0", md5="fc60c2018580decaea30f09de55142fb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation