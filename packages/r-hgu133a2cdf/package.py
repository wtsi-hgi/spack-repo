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

	version("2.18.0", sha256="ea0f7bcd3468d939e8b41bc251c7a871986f75b072df2da7217a7070f7a71453")

	depends_on("r-annotationdbi", type=("build", "run"))

