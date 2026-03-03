# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34acdf(RPackage):
	"""rgu34acdf

	A package containing an environment representing the RG_U34A.cdf file.
	"""
	
	bioc = "rgu34acdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34acdf/rgu34acdf_2.18.0.tar.gz"]

	version("2.18.0", md5="dcfa7ecce00e529f93809759ed837b8d")

	depends_on("r-annotationdbi", type=("build", "run"))

