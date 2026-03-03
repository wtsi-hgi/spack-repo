# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfaDimensions(RPackage):
	"""Exploratory Factor Analysis Functions for Assessing
Dimensionality

	Functions for eleven procedures for determining the number of 
    factors, including functions for parallel analysis and the minimum average partial 
    test. There are also functions for conducting principal components analysis, principal 
    axis factor analysis, maximum likelihood factor analysis, image factor analysis, 
    and extension factor analysis, all of which can take raw data or correlation matrices 
    as input and with options for conducting the analyses using Pearson correlations, 
    Kendall correlations, Spearman correlations, gamma correlations, or polychoric 
    correlations. Varimax rotation, promax rotation, and Procrustes rotations can be
    performed. Additional functions focus on the factorability of a correlation matrix,
    the congruences between factors from different datasets, the assessment of local
    independence, the assessment of factor solution complexity, and internal consistency.
    Auerswald & Moshagen (2019, ISSN:1939-1463);
    Field, Miles, & Field (2012, ISBN:978-1-4462-0045-2);
    Mulaik (2010, ISBN:978-1-4200-9981-2);
    O'Connor (2000, <doi:10.3758/bf03200807>);
    O'Connor (2001, ISSN:0146-6216).
	"""
	
	cran = "EFA.dimensions" 

	version("0.1.8.1", md5="3256ae51820f077a99469df53520e377")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-efatools", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
