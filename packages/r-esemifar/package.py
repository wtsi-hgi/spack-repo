# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsemifar(RPackage):
	"""Smoothing Long-Memory Time Series

	The nonparametric trend and its derivatives in equidistant time 
    series (TS) with long-memory errors can be estimated. The 
    estimation is conducted via local polynomial regression using an 
    automatically selected bandwidth obtained by a built-in iterative plug-in 
    algorithm or a bandwidth fixed by the user.
    The smoothing methods of the package are described in Letmathe, S., Beran,
    J. and Feng, Y., (2021) <https://ideas.repec.org/p/pdn/ciepap/145.html>.
	"""
	
	homepage = "https://wiwi.uni-paderborn.de/en/dep4/feng/"
	cran = "esemifar" 

	version("1.0.2", md5="311e818b073eb3ca2a5c5c561898d077")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-smoots", type=("build", "run"))
