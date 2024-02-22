# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivedriver(RPackage):
	"""Finding Cancer Driver Proteins with Enriched Mutations in
Post-Translational Modification Sites

	A mutation analysis tool that discovers cancer driver genes with frequent mutations in protein signalling sites such as post-translational modifications (phosphorylation, ubiquitination, etc). The Poisson generalised linear regression model identifies genes where cancer mutations in signalling sites are more frequent than expected from the sequence of the entire gene. Integration of mutations with signalling information helps find new driver genes and propose candidate mechanisms to known drivers. Reference: Systematic analysis of somatic mutations in phosphorylation signaling predicts novel cancer drivers. Juri Reimand and Gary D Bader. Molecular Systems Biology (2013) 9:637 <doi:10.1038/msb.2012.68>.
	"""
	
	cran = "ActiveDriver" 

	version("1.0.0", md5="b42082d5369e339f36c5a171c1c1848e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
