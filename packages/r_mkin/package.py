# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkin(RPackage):
	"""Kinetic Evaluation of Chemical Degradation Data

	Calculation routines based on the FOCUS Kinetics Report (2006,
  2014).  Includes a function for conveniently defining differential equation
  models, model solution based on eigenvalues if possible or using numerical
  solvers.  If a C compiler (on windows: 'Rtools') is installed, differential
  equation models are solved using automatically generated C functions.
  Heteroscedasticity can be taken into account using variance by variable or
  two-component error models as described by Ranke and Meinecke (2018)
  <doi:10.3390/environments6120124>.  Hierarchical degradation models can
  be fitted using nonlinear mixed-effects model packages as a back end as
  described by Ranke et al. (2021) <doi:10.3390/environments8080071>.  Please
  note that no warranty is implied for correctness of results or fitness for a
  particular purpose.
	"""
	
	homepage = "https://pkgdown.jrwb.de/mkin/"
	cran = "mkin" 

	version("1.2.6", md5="afd675e37b65469529c3e20ced670d74")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-desolve@1.35:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-inline@0.3.19:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("r-nlme@3.1.151:", type=("build", "run"))
	depends_on("r-saemix@3.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
