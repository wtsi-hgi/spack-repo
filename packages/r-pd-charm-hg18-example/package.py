# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdCharmHg18Example(RPackage):
	"""Platform Design Info for NimbleGen charm_hg18_example

	Platform Design Info for NimbleGen charm_hg18_example
	"""
	
	bioc = "pd.charm.hg18.example" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.charm.hg18.example_0.99.4.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.charm.hg18.example/pd.charm.hg18.example_0.99.4.tar.gz"]

	version("0.99.4", sha256="2fcb90dfeab1a18eeba6707cc217730d960e443225d944f0b97ba0fb091c1b5b")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rsqlite@0.7.1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.9.30:", type=("build", "run"))
	depends_on("r-oligo@1.11.18:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings@2.29.2:", type=("build", "run"))
	depends_on("r-iranges@1.19.5:", type=("build", "run"))

