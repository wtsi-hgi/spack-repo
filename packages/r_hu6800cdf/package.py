# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu6800cdf(RPackage):
	"""hu6800cdf

	A package containing an environment representing the Hu6800.CDF file.
	"""
	
	bioc = "hu6800cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu6800cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu6800cdf/hu6800cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="fa2b2ab8f3aba517c63ad2e65873d2f0")

	depends_on("r-annotationdbi", type=("build", "run"))

