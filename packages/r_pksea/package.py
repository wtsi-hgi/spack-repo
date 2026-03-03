# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPksea(RPackage):
	"""Prediction-Based Kinase-Substrate Enrichment Analysis

	A tool for inferring kinase activity changes from 
    phosphoproteomics data. 'pKSEA' uses kinase-substrate 
    prediction scores to weight observed changes in 
    phosphopeptide abundance to calculate a phosphopeptide-level 
    contribution score, then sums up these contribution scores by 
    kinase to obtain a phosphoproteome-level kinase activity 
    change score (KAC score). 'pKSEA' then assesses the 
    significance of changes in predicted substrate abundances for 
    each kinase using permutation testing. This results in a 
    permutation score (pKSEA significance score) reflecting the 
    likelihood of a similarly high or low KAC from random chance, 
    which can then be interpreted in an analogous manner to an 
    empirically calculated p-value. 'pKSEA' contains default 
    databases of kinase-substrate predictions from 'NetworKIN' 
    (NetworKINPred_db) <http://networkin.info> 
    Horn, et. al (2014) <doi:10.1038/nmeth.2968>
    and of known kinase-substrate links from 'PhosphoSitePlus' 
    (KSEAdb) <https://www.phosphosite.org/>
    Hornbeck PV, et. al (2015) <doi:10.1093/nar/gku1267>.
	"""
	
	cran = "pKSEA" 

	version("0.0.1", md5="8f4e0d3b8cdb7c48f6ce30d1f3cd9627")

	depends_on("r@3.3:", type=("build", "run"))
