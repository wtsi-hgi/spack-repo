# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAth1121501cdf(RPackage):
	"""ath1121501cdf

	A package containing an environment representing the ATH1-121501.CDF file.
	"""
	
	bioc = "ath1121501cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ath1121501cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ath1121501cdf/ath1121501cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="8b63798143219b7c1c2666a91a1a2440")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation