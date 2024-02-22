# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdFeinbergMm8MeHx1(RPackage):
	"""Platform Design Info for NimbleGen feinberg_mm8_me_hx1

	Platform Design Info for NimbleGen feinberg_mm8_me_hx1
	"""
	
	bioc = "pd.feinberg.mm8.me.hx1" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.feinberg.mm8.me.hx1_0.99.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/pd.feinberg.mm8.me.hx1/pd.feinberg.mm8.me.hx1_0.99.3.tar.gz"]

	version("0.99.3", md5="7332102b69fc9ee087f52d3cdc311d00", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.feinberg.mm8.me.hx1_0.99.3.tar.gz")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rsqlite@0.7.1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.9.30:", type=("build", "run"))
	depends_on("r-oligo@1.11.18:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings@2.13.50:", type=("build", "run"))
	depends_on("r-iranges@1.3.89:", type=("build", "run"))

	# annotation