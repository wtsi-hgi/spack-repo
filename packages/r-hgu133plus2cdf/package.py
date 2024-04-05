# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133plus2cdf(RPackage):
	"""hgu133plus2cdf

	A package containing an environment representing the HG-U133_Plus_2.cdf file.
	"""
	
	bioc = "hgu133plus2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133plus2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133plus2cdf/hgu133plus2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="284fef2f0b777d7b53451538ddd53de3")

	depends_on("r-annotationdbi", type=("build", "run"))

