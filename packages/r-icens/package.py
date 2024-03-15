# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcens(RPackage):
	"""NPMLE for Censored and Truncated Data

	Many functions for computing the NPMLE for censored and truncated data.
	"""
	
	bioc = "Icens" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Icens_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Icens/Icens_1.74.0.tar.gz"]

	version("1.74.0", md5="07481f23c5b4fdfe9ff465e5a57e33c2")

	depends_on("r-survival", type=("build", "run"))
