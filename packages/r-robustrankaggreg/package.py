# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustrankaggreg(RPackage):
	"""Methods for Robust Rank Aggregation

	Methods for aggregating ranked lists, especially lists of
    genes. It implements the Robust Rank Aggregation Kolde et al (2012)
    <doi:10.1093/bioinformatics/btr709> and some other simple algorithms 
    for the task. RRA method uses a probabilistic model for aggregation that 
    is robust to noise and also facilitates the calculation of significance
    probabilities for all the elements in the final ranking.
	"""
	
	cran = "RobustRankAggreg" 

	version("1.2.1", md5="76c896a3ebc71bcab67a43e87e716ee8")

