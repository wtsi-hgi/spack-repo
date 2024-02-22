# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkea(RPackage):
	"""R/KEA Interface

	An R interface to KEA (Version 5.0).
  KEA (for Keyphrase Extraction Algorithm) allows for extracting
  keyphrases from text documents. It can be either used for free
  indexing or for indexing with a controlled vocabulary. For more
  information see <http://www.nzdl.org/Kea/>.
	"""
	
	cran = "RKEA" 

	version("0.0-6", md5="ba5699a2a5bdad288ca6062385e931f9")

	depends_on("r-rkeajars@5.0.1:", type=("build", "run"))
	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
