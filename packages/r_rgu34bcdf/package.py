# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34bcdf(RPackage):
	"""rgu34bcdf

	A package containing an environment representing the RG_U34B.cdf file.
	"""
	
	bioc = "rgu34bcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34bcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34bcdf/rgu34bcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="428b3a39f0d8addd7d863539b8cda6ea")

	depends_on("r-annotationdbi", type=("build", "run"))

