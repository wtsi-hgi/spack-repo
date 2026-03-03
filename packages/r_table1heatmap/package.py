# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTable1heatmap(RPackage):
	"""Table 1 Heatmap

	Table 1 is the classical way to describe the patients in a
    clinical study. The amount of splits in the data in such a table is
    limited. Table1Heatmap draws a heatmap of all crosstables that can be
    generated with the data. Users can choose between showing the actual
    crosstables or direction of effect of associations, and highlight
    associations by number of patients or p-values.
    v1.2 - fixed "missing "no visible global function definition for .."
	"""
	
	cran = "Table1Heatmap" 

	version("1.2", md5="390b04475665a26b8da6e390c85189bb")

	depends_on("r-colorramps", type=("build", "run"))
