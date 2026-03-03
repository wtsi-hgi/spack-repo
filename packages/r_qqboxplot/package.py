# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQqboxplot(RPackage):
	"""Implementation of the Q-Q Boxplot

	A system to implement the Q-Q boxplot.  It is implemented as an
    extension to 'ggplot2'.  The Q-Q boxplot is an amalgam of the boxplot and the
    Q-Q plot and allows the user to rapidly examine summary statistics and tail
    behavior for multiple distributions in the same pane.  As an extension of
    the 'ggplot2' implementation of the boxplot, possible modifications to the 
    boxplot extend to the Q-Q boxplot.
	"""
	
	cran = "qqboxplot" 

	version("0.3.0", md5="244fd7115fd0a3f58740acfddf00854c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
