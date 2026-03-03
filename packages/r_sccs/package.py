# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSccs(RPackage):
	"""The Self-Controlled Case Series Method

	Various self-controlled case series models used to investigate 
        associations between time-varying exposures such as vaccines or
        other drugs or non drug exposures and an adverse event can be
        fitted. Detailed information on the self-controlled case series
        method and its extensions with more examples can be found in 
        Farrington, P., Whitaker, H., and Ghebremichael Weldeselassie, Y.
        (2018, ISBN: 978-1-4987-8159-6. Self-controlled Case Series studies:
        A modelling Guide with R. Boca Raton: Chapman & Hall/CRC Press) 
        and <https://sccs-studies.info/index.html>.
	"""
	
	cran = "SCCS" 

	version("1.7", md5="89f4b5382c00ef90316a404d7633e493")
	version("1.6", md5="375a24327e8dff8d9497745bfb5c74b1")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
