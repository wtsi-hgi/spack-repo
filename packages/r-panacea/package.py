# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanacea(RPackage):
	"""Personalized Network-Based Anti-Cancer Therapy Evaluation

	Identification of the most appropriate pharmacotherapy for each 
    patient based on genomic alterations is a major challenge in personalized 
    oncology. 'PANACEA' is a collection of personalized anti-cancer drug 
    prioritization approaches utilizing network methods. The methods utilize 
    personalized "driverness" scores from 'driveR' to rank drugs, mapping these
    onto a protein-protein interaction network. The "distance-based" method 
    scores each drug based on these scores and distances between drugs and genes
    to rank given drugs. The "RWR" method propagates these scores via a 
    random-walk with restart framework to rank the drugs. The methods are 
    described in detail in Ulgen E, Ozisik O, Sezerman OU. 2023. PANACEA: 
    network-based methods for pharmacotherapy prioritization in personalized 
    oncology. Bioinformatics <doi:10.1093/bioinformatics/btad022>.
	"""
	
	homepage = "https://github.com/egeulgen/PANACEA"
	cran = "PANACEA" 

	version("1.0.1", md5="06eca1906e478ad674b329c583f02b18")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
