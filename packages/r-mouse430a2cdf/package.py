# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse430a2cdf(RPackage):
	"""mouse430a2cdf

	A package containing an environment representing the Mouse430A_2.cdf file.
	"""
	
	bioc = "mouse430a2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse430a2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse430a2cdf/mouse430a2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="1114c0415d1200bc21ad205e0830b075")

	depends_on("r-annotationdbi", type=("build", "run"))

