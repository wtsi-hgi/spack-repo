# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNugohs1a520180cdf(RPackage):
	"""nugohs1a520180cdf

	A package containing an environment representing the NuGO_Hs1a520180.cdf file.
	"""
	
	bioc = "nugohs1a520180cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/nugohs1a520180cdf_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/nugohs1a520180cdf/nugohs1a520180cdf_3.4.0.tar.gz"]

	version("3.4.0", md5="aa152658a4a801cc0edb552a98aee841")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

