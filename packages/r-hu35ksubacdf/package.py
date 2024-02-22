# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubacdf(RPackage):
	"""hu35ksubacdf

	A package containing an environment representing the Hu35KsubA.CDF file.
	"""
	
	bioc = "hu35ksubacdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hu35ksubacdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hu35ksubacdf/hu35ksubacdf_2.18.0.tar.gz"]

	version("2.18.0", md5="c8b82c4755eb62818ca0dbf22de5d25e")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation