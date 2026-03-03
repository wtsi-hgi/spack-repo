# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlagr(RPackage):
	"""Implementation of Flag Aggregation

	Three methods are implemented in R to facilitate the aggregations of flags in official statistics.  
            From the underlying flags the highest in the hierarchy, the most frequent, or with the highest total weight
            is propagated to the flag(s) for EU or other aggregates. Below there are some reference documents for the topic: 
            <https://sdmx.org/wp-content/uploads/CL_OBS_STATUS_v2_1.docx>,
            <https://sdmx.org/wp-content/uploads/CL_CONF_STATUS_1_2_2018.docx>,
            <http://ec.europa.eu/eurostat/data/database/information>,
            <http://www.oecd.org/sdd/33869551.pdf>,
            <https://sdmx.org/wp-content/uploads/CL_OBS_STATUS_implementation_20-10-2014.pdf>.
	"""
	
	cran = "flagr" 

	version("0.3.2", md5="63ce686d95373f0230d561d5b17f18fe")

