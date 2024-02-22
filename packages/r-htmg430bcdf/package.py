# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430bcdf(RPackage):
	"""htmg430bcdf

	A package containing an environment representing the HT_MG-430B.cdf file.
	"""
	
	bioc = "htmg430bcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/htmg430bcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/htmg430bcdf/htmg430bcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="53cc1408504a5f07b5655aa46b969157")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation