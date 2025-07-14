# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhosphonormalizer(RPackage):
	"""Compensates for the bias introduced by median normalization in

	It uses the overlap between enriched and non-enriched datasets to compensate for the bias introduced in global phosphorylation after applying median normalization.
	"""
	
	bioc = "phosphonormalizer" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/phosphonormalizer_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/phosphonormalizer/phosphonormalizer_1.26.0.tar.gz"]

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="31f5bdbb7b8e318807c234ef512a57df12fc88e1aeb16097bd4dc0095cdb49f7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
