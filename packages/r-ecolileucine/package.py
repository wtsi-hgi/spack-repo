# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolileucine(RPackage):
	"""Experimental data with Affymetrix E. coli chips

	Experimental data with Affymetrix E. coli chips, as reported in She-pin Hung, Pierre Baldi, and G. Wesley Hatfield, J. Biol. Chem., Vol. 277, Issue 43, 40309-40323, October 25, 2002
	"""
	
	bioc = "ecoliLeucine" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ecoliLeucine_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ecoliLeucine/ecoliLeucine_1.42.0.tar.gz"]

	version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="5cc5398bfc997d90cbcb0a1974312eadfeea9bb31bf730ca17b17186d186620b")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-ecolicdf", type=("build", "run"))

