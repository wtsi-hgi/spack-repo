# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133a2cdf(RPackage):
	"""hgu133a2cdf

	A package containing an environment representing the HG-U133A_2.cdf file.
	"""
	
	bioc = "hgu133a2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133a2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133a2cdf/hgu133a2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="566bc70f0bb94a376bf88f191a2f067e")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation