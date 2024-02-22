# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoplarcdf(RPackage):
	"""poplarcdf

	A package containing an environment representing the Poplar.cdf file.
	"""
	
	bioc = "poplarcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/poplarcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/poplarcdf/poplarcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="556e7f8f6f76436552d8044ef29279cb")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation