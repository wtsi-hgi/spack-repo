# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRroad(RPackage):
	"""Road Condition Analysis

	Computation of the International Roughness Index (IRI) given a
    longitudinal road profile. The IRI can be calculated for a single road segment
    or for a sequence of segments with a fixed length (e. g. 100m). For the latter,
    an overlap of the segments can be selected. The IRI and likewise the algorithms
    for its determination are defined in Sayers, Michael W; Gillespie, Thomas D;
    Queiroz, Cesar A.V. 1986. The International Road Roughness Experiment (IRRE) :
    establishing correlation and a calibration standard for measurements. World
    Bank technical paper; no. WTP 45. Washington, DC : The World Bank. (ISBN
    0-8213-0589-1) available from <http://documents.worldbank.org/curated/en/326081468740204115>.
	"""
	
	homepage = "http://github.com/vsimko/rroad"
	cran = "rroad" 

	version("0.0.5", md5="9cab265438ed1963c879429b1c5bef20")

