# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQicharts2(RPackage):
	"""Quality Improvement Charts

	Functions for making run charts, Shewhart control charts and
    Pareto charts for continuous quality improvement. Included control charts
    are: I, MR, Xbar, S, T, C, U, U', P, P', and G charts. Non-random variation
    in the form of minor to moderate persistent shifts in data over time is
    identified by the Anhoej rules for unusually long runs and unusually few
    crossing  [Anhoej, Olesen (2014) <doi:10.1371/journal.pone.0113825>].
    Non-random variation in the form of larger, possibly transient, shifts is
    identified by Shewhart's 3-sigma rule [Mohammed, Worthington, Woodall (2008)
    <doi:10.1136/qshc.2004.012047>].
	"""
	
	homepage = "https://github.com/anhoej/qicharts2"
	cran = "qicharts2" 

	version("0.7.4", md5="2ec5283fe59b771c64325059dd7df952", url="https://cran.r-project.org/src/contrib/qicharts2_0.7.4.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
