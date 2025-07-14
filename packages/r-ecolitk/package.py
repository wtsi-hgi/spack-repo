# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolitk(RPackage):
	"""Meta-data and tools for E. coli

	Meta-data and tools to work with E. coli. The tools are mostly plotting functions to work with circular genomes. They can used with other genomes/plasmids.
	"""
	
	bioc = "ecolitk" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ecolitk_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ecolitk/ecolitk_1.74.0.tar.gz"]

	version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="a3f0d59fd409127b6b8abc6a4654f9aa4f4bf5d52293eb14cbfb5393912ab8cd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
