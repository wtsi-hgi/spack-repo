# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSadisa(RPackage):
	"""Species Abundance Distributions with Independent-Species
Assumption

	Computes the probability of a set of species abundances of a single or multiple samples of individuals with one or more guilds under a mainland-island model. One must specify the mainland (metacommunity) model and the island (local) community model. It assumes that species fluctuate independently. The package also contains functions to simulate under this model. See Haegeman, B. & R.S. Etienne (2017). A general sampling formula for community structure data. Methods in Ecology & Evolution 8: 1506-1519 <doi:10.1111/2041-210X.12807>. 
	"""
	
	cran = "SADISA" 

	version("1.2", md5="1d4ca4a3a10f2f24612049a7c670317a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ddd@4.1:", type=("build", "run"))
