# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeather(RPackage):
	"""R Bindings to the Feather 'API'

	Read and write feather files, a lightweight binary columnar
    data store designed for maximum speed.
	"""
	
	homepage = "https://github.com/wesm/feather"
	cran = "feather" 

	version("0.3.5", md5="dd1a90af493a0dd721122d119bf694ad")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
