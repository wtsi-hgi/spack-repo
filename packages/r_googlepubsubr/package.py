# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglepubsubr(RPackage):
	"""R Interface for Google 'Cloud Pub/Sub' REST API

	Provides an easy to use interface to the 'Google
	Pub/Sub' REST API <https://cloud.google.com/pubsub/docs/reference/rest>.
	"""
	
	homepage = "https://github.com/andodet/googlePubsubR"
	cran = "googlePubsubR" 

	version("0.0.4", md5="604c287a81835ac43ada49f01874c654")

	depends_on("r-googleauthr@0.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
