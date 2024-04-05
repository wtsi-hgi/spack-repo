# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXenopuslaeviscdf(RPackage):
	"""xenopuslaeviscdf

	A package containing an environment representing the Xenopus_laevis.cdf file.
	"""
	
	bioc = "xenopuslaeviscdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/xenopuslaeviscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/xenopuslaeviscdf/xenopuslaeviscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="9d09ff76471ae60faf71090e0638f240")

	depends_on("r-annotationdbi", type=("build", "run"))

