# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RU133x3pcdf(RPackage):
	"""u133x3pcdf

	A package containing an environment representing the U133_X3P.cdf file.
	"""
	
	bioc = "u133x3pcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/u133x3pcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/u133x3pcdf/u133x3pcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="ee4e62041bc8c63813e8cf8400ece2f3")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation