# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkovchart(RPackage):
	"""Markov Chain-Based Cost-Optimal Control Charts

	Functions for cost-optimal control charts with a focus on health care applications. Compared to assumptions in traditional control chart theory, here, we allow random shift sizes, random repair and random sampling times. The package focuses on X-bar charts with a sample size of 1 (representing the monitoring of a single patient at a time). The methods are described in Zempleni et al. (2004) <doi:10.1002/asmb.521>, Dobi and Zempleni (2019) <doi:10.1002/qre.2518> and Dobi and Zempleni (2019) <http://ac.inf.elte.hu/Vol_049_2019/129_49.pdf>.
	"""
	
	cran = "Markovchart" 

	version("2.1.5", md5="f5e251f0506b56a1586aa593afcc6f13")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
