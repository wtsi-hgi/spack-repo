# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProscorertools(RPackage):
	"""Tools to Score Patient-Reported Outcome (PRO) and Other
Psychometric Measures

	Provides a reliable and flexible toolbox to score 
    patient-reported outcome (PRO), Quality of Life (QOL), and other 
    psychometric measures. The guiding philosophy is that scoring errors can 
    be eliminated by using a limited number of well-tested, well-behaved 
    functions to score PRO-like measures. The workhorse of the package is 
    the 'scoreScale' function, which can be used to score most single-scale 
    measures. It can reverse code items that need to be reversed before 
    scoring and pro-rate scores for missing item data. Currently, three 
    different types of scores can be output: summed item scores, mean item 
    scores, and scores scaled to range from 0 to 100. The 'PROscorerTools' 
    functions can be used to write new functions that score more complex 
    measures. In fact, 'PROscorerTools' functions are the building blocks of 
    the scoring functions in the 'PROscorer' package (which is a repository 
    of functions that score specific commonly-used instruments). Users are 
    encouraged to use 'PROscorerTools' to write scoring functions for their 
    favorite PRO-like instruments, and to submit these functions for 
    inclusion in 'PROscorer' (a tutorial vignette will be added soon). The 
    long-term vision for the 'PROscorerTools' and 'PROscorer' packages is to 
    provide an easy-to-use system to facilitate the incorporation of PRO 
    measures into research studies in a scientifically rigorous and 
    reproducible manner. These packages and their vignettes are intended to 
    help establish and promote "best practices" for scoring and describing 
    PRO-like measures in research. 
	"""
	
	homepage = "https://github.com/MSKCC-Epi-Bio/PROscorerTools"
	cran = "PROscorerTools" 

	version("0.0.4", md5="4e668d300d95c139b377c5fc491a54fe")

