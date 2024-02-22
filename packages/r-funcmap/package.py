# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuncmap(RPackage):
	"""Hive Plots of R Package Function Calls

	Analyzes the function calls in an R package and creates a hive plot of the calls, dividing them among functions that only make outgoing calls (sources), functions that have only incoming calls (sinks), and those that have both incoming calls and make outgoing calls (managers).  Function calls can be mapped by their absolute numbers, their normalized absolute numbers, or their rank.  FuncMap should be useful for comparing packages at a high level for their overall design.  Plus, it's just plain fun.  The hive plot concept was developed by Martin Krzywinski (www.hiveplot.com) and inspired this package.  Note: this package is maintained for historical reasons. HiveR is a full package for creating hive plots.
	"""
	
	cran = "FuncMap" 

	version("1.0.10", md5="33dce28ba9d934c91bdc9adac99c220a")

	depends_on("r-mvbutils", type=("build", "run"))
