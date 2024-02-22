# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelaggregation(RPackage):
	"""Aggregate Longitudinal Survey Data

	Aggregate Business Tendency Survey Data (and other qualitative
    surveys) to time series at various aggregation levels. Run aggregation of
    survey data in a speedy, re-traceable and a easily deployable way.
    Aggregation is substantially accelerated by use of data.table.
    This package intends to provide an interface that is less general and abstract than data.table but rather geared towards
    survey researchers.
	"""
	
	cran = "panelaggregation" 

	version("0.1.1", md5="26967b822dce60c208579ea45168d5c9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
