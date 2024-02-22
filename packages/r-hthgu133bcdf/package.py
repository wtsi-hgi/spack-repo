# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133bcdf(RPackage):
	"""hthgu133bcdf

	A package containing an environment representing the HT_HG-U133B.cdf file.
	"""
	
	bioc = "hthgu133bcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hthgu133bcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hthgu133bcdf/hthgu133bcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="935ae53fb168d9c7890d71020ef4c366")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation