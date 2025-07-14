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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AWFisher_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AWFisher/AWFisher_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="3a21d029ffeea5f64eb720af4c29a5bf867095178d357ca6215c7c4040c48581")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
