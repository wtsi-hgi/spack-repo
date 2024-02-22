# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProscorer(RPackage):
	"""Functions to Score Commonly-Used Patient-Reported Outcome (PRO)
Measures and Other Psychometric Instruments

	An extensible repository of accurate, up-to-date functions to
    score commonly used patient-reported outcome (PRO), quality of life
    (QOL), and other psychometric and psychological measures.
    'PROscorer', together with the 'PROscorerTools' package, is a system
    to facilitate the incorporation of PRO measures into research studies
    and clinical settings in a scientifically rigorous and reproducible
    manner.  These packages and their vignettes are intended to help
    establish and promote best practices for scoring PRO and PRO-like 
    measures in research.  The 'PROscorer' Instrument Descriptions vignette 
    contains descriptions of each instrument scored by 'PROscorer', complete 
    with references.  These instrument descriptions are suitable for inclusion 
    in formal study protocol documents, grant proposals, and manuscript Method
    sections.  Each 'PROscorer' function is composed of helper functions
    from the 'PROscorerTools' package, and users are encouraged to
    contribute new functions to 'PROscorer'.  More scoring functions are
    currently in development and will be added in future updates.
	"""
	
	homepage = "https://github.com/raybaser/PROscorer"
	cran = "PROscorer" 

	version("0.0.4", md5="c3126276ca98ca62ba71d74aea2ca7c7")

	depends_on("r-proscorertools", type=("build", "run"))
