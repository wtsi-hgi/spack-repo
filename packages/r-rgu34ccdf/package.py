# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34ccdf(RPackage):
	"""rgu34ccdf

	A package containing an environment representing the RG_U34C.cdf file.
	"""
	
	bioc = "rgu34ccdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34ccdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34ccdf/rgu34ccdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="3de442fcc7447938de708a2770b79a8c13ee86cb06d36dbd1ee7f1e5b5a2cf6c")

	depends_on("r-annotationdbi", type=("build", "run"))

