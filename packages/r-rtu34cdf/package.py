# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtu34cdf(RPackage):
	"""rtu34cdf

	A package containing an environment representing the RT_U34.cdf file.
	"""
	
	bioc = "rtu34cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rtu34cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rtu34cdf/rtu34cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="662413be163a7d7fe99e00995fafd9c13269763d1a6341f3420c0834b7e5c581")

	depends_on("r-annotationdbi", type=("build", "run"))

