# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaroline(RPackage):
	"""A Collection of Database, Data Structure, Visualization, andUtility
	Functions for R.

	The caroline R library contains dozens of functions useful for: database
	migration (dbWriteTable2), database style joins & aggregation (nerge,
	groupBy & bestBy), data structure conversion (nv, tab2df), legend table
	making (sstable & leghead), plot annotation (labsegs & mvlabs), data
	visualization (violins, pies & raPlot), character string manipulation (m &
	pad), file I/O (write.delim), batch scripting and more. The package's
	greatest contributions lie in the database style merge, aggregation and
	interface functions as well as in it's extensive use and propagation of
	row, column and vector names in most functions."""

	cran = "caroline"

	version("0.9.2", md5="f54822c8114a622ea1cb8794be66c930")

	depends_on("r@2:", type=("build", "run"))
