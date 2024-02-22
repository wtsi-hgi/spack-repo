# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdherer(RPackage):
	"""Adherence to Medications

	Computation of adherence to medications from Electronic Health care 
    Data and visualization of individual medication histories and adherence 
    patterns. The package implements a set of S3 classes and
    functions consistent with current adherence guidelines and definitions. 
    It allows the computation of different measures of
    adherence (as defined in the literature, but also several original ones), 
    their publication-quality plotting,
    the estimation of event duration and time to initiation,
    the interactive exploration of patient medication history and 
    the real-time estimation of adherence given various parameter settings.
    It scales from very small datasets stored in flat CSV files to very large 
    databases and from single-thread processing on mid-range consumer
    laptops to parallel processing on large heterogeneous computing clusters.
    It exposes a standardized interface allowing it to be used from other
    programming languages and platforms, such as Python.
	"""
	
	homepage = "https://github.com/ddediu/AdhereR"
	cran = "AdhereR" 

	version("0.8.1", md5="0464eaadbcb6931ff5e046836834f357")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lubridate@1.5:", type=("build", "run"))
	depends_on("r-data-table@1.9:", type=("build", "run"))
	depends_on("r-rsvg@1.3:", type=("build", "run"))
	depends_on("r-jpeg@0.1:", type=("build", "run"))
	depends_on("r-png@0.1:", type=("build", "run"))
	depends_on("r-webp@1:", type=("build", "run"))
