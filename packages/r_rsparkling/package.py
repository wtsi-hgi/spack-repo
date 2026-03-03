# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsparkling(RPackage):
	"""R Interface for H2O Sparkling Water

	An extension package for 'sparklyr' that provides an R interface to
    H2O Sparkling Water machine learning library (see <https://github.com/h2oai/sparkling-water> for more information).
	"""
	
	homepage = "https://github.com/h2oai/sparkling-water/tree/master/r"
	cran = "rsparkling" 

	version("0.2.19", md5="37db6b61110f5d1853b489f9264c5d44")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sparklyr@0.3:", type=("build", "run"))
	depends_on("r-h2o@3.8.3.3:", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
