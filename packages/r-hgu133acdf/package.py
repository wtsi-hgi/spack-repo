# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133acdf(RPackage):
	"""hgu133acdf

	A package containing an environment representing the HG-U133A.cdf file.
	"""
	
	bioc = "hgu133acdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgu133acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgu133acdf/hgu133acdf_2.18.0.tar.gz"]

	version("2.18.0", md5="d3e0e22b2d3943d26c94e7c01b91035c")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation