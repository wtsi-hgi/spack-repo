# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKidpack(RPackage):
	"""DKFZ kidney package

	kidney microarray data
	"""
	
	homepage = "http://www.dkfz.de/mga"
	bioc = "kidpack" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/kidpack_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/kidpack/kidpack_1.44.0.tar.gz"]

	version("1.44.0", md5="26f5ad5fba1c63156e282d8eac7ac385")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

	# experiment