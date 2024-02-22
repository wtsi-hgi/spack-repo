# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMountainplot(RPackage):
	"""Mountain Plots, Folded Empirical Cumulative Distribution Plots

	Lattice functions for drawing folded empirical cumulative
    distribution plots, or mountain plots. A mountain plot is similar
    to an empirical CDF plot, except that the curve increases from
    0 to 0.5, then decreases from 0.5 to 1 using an inverted scale at
    the right side. See Monti (1995) <doi:10.1080/00031305.1995.10476179>.
	"""
	
	homepage = "https://kwstat.github.io/mountainplot/"
	cran = "mountainplot" 

	version("1.4", md5="3fe5797165a92649c68cb4bede9a6de5")

	depends_on("r-lattice", type=("build", "run"))
