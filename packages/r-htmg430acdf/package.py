# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430acdf(RPackage):
	"""htmg430acdf

	A package containing an environment representing the HT_MG-430A.cdf file.
	"""
	
	bioc = "htmg430acdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htmg430acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htmg430acdf/htmg430acdf_2.18.0.tar.gz"]

	version("2.18.0", md5="aef7a3c3af7d2624ee6fc6f2d22472e2")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation