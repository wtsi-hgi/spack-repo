# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcspikelite(RPackage):
	"""Spike-in data for GC/MS data and methods within flagme

	Spike-in data for GC/MS data and methods within flagme
	"""
	
	bioc = "gcspikelite" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/gcspikelite_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/gcspikelite/gcspikelite_1.40.0.tar.gz"]

	version("1.40.0", sha256="c5c9a4728e5491d5ff0e462d393f23d8564b1d755a68a7bcd4c6c7304dbad5f9")

	depends_on("r@2.5:", type=("build", "run"))

