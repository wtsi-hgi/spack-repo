# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmpaffyexample(RPackage):
	"""Example of Amplified Data

	Six arrays. Three from amplified RNA, three from the typical procedure.
	"""
	
	homepage = "https://bioconductor.org/packages/AmpAffyExample"
	bioc = "AmpAffyExample" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/AmpAffyExample_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/AmpAffyExample/AmpAffyExample_1.42.0.tar.gz"]

	version("1.42.0", md5="3277d6d26f145ddbb45c3808273cd150")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

	# experiment