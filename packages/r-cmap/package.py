# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmap(RPackage):
	"""A data package containing annotation data for cMAP

	Annotation data file for cMAP assembled using data from public data repositories
	"""
	
	bioc = "cMAP" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/cMAP_1.15.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/cMAP/cMAP_1.15.1.tar.gz"]

	version("1.15.1", md5="dbf8df4d4540151936884e1c5d747bcf")

	depends_on("r@2.4:", type=("build", "run"))

	# annotation