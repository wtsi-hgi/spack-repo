# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTest3cdf(RPackage):
	"""test3cdf

	A package containing an environment representing the Test3.CDF file.
	"""
	
	bioc = "test3cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/test3cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/test3cdf/test3cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="9904e7fa6599f68400a9b77d0caa159a")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation