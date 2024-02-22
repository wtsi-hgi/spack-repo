# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdata(RPackage):
	"""Prepare Your Time-Series Data for Further Analysis

	Provides a set of tools for managing time-series data,
    with a particular emphasis on defining various frequency types such
    as daily and weekly. It also includes functionality for converting
    data between different frequencies.
	"""
	
	homepage = "https://github.com/rmojab63/LDT"
	cran = "tdata" 

	version("0.3.0", md5="3d07736d5f1af05d5e2fcfab16d7f821")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
