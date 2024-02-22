# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwfisher(RPackage):
	"""An R package for fast computing for adaptively weighted fisher's method

	Implementation of the adaptively weighted fisher's method, including fast p-value computing, variability index, and meta-pattern.
	"""
	
	bioc = "AWFisher" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AWFisher_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AWFisher/AWFisher_1.16.0.tar.gz"]

	version("1.16.0", md5="ba9b2824782018cc7626ebc72b6bb81e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
