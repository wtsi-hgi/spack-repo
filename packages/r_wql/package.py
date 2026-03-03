# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWql(RPackage):
	"""Exploring Water Quality Monitoring Data

	Functions to assist in the processing and
    exploration of data from environmental monitoring programs.
    The package name stands for "water quality" and reflects the
    original focus on time series data for physical and chemical
    properties of water, as well as the biota. Intended for
    programs that sample approximately monthly, quarterly or
    annually at discrete stations, a feature of many legacy data
    sets. Most of the functions should be useful for analysis of
    similar-frequency time series regardless of the subject
    matter.
	"""
	
	homepage = "https://github.com/jsta/wql"
	cran = "wql" 

	version("1.0.0", md5="d491d46fa355e89be310affdb6bd0001")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
