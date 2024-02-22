# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHddplot(RPackage):
	"""Use Known Groups in High-Dimensional Data to Derive Scores for
Plots

	Cross-validated linear discriminant calculations determine
  the optimum number of features. Test and training scores from
  successive cross-validation steps determine, via a principal
  components calculation, a low-dimensional global space onto which test
  scores are projected, in order to plot them. Further functions are
  included that are intended for didactic use. The  package implements,
  and extends, methods described in J.H. Maindonald and C.J. Burden (2005)
  <https://journal.austms.org.au/V46/CTAC2004/Main/home.html>.
	"""
	
	homepage = "https://github.com/jhmaindonald/hddplot"
	cran = "hddplot" 

	version("0.59-2", md5="af987346c2df7bf9d094ea5351535848")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
