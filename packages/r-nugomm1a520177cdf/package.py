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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/nugomm1a520177cdf_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/nugomm1a520177cdf/nugomm1a520177cdf_3.4.0.tar.gz"]

	version("3.4.0", sha256="ca24c99dd2283a1419d6a952d7a92ac5c8a082230fe2327ff31b446dce2a6d6a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

