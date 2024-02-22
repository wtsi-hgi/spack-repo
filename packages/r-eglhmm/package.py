# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REglhmm(RPackage):
	"""Extended Generalised Linear Hidden Markov Models

	Fits a variety of hidden Markov models, structured
	in an extended generalized linear model framework.  See
	T. Rolf Turner, Murray A. Cameron, and Peter J. Thomson
	(1998) <doi:10.2307/3315677>, and
	Rolf Turner (2008) <doi:10.1016/j.csda.2008.01.029>
	and the references cited therein.
	"""
	
	cran = "eglhmm" 

	version("0.1-3", md5="baa5fb77fa588cb19bb3d985e8e6df86")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbd", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
