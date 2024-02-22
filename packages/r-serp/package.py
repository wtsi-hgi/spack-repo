# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSerp(RPackage):
	"""Smooth Effects on Response Penalty for CLM

	A regularization method for the cumulative link
    models.  The smooth-effect-on-response penalty (SERP) provides
    flexible modelling of the ordinal model by enabling the smooth
    transition from the general cumulative link model to a coarser form of
    the same model. In other words, as the tuning parameter goes from zero
    to infinity, the subject-specific effects associated with each
    variable in the model tend to a unique global effect. The parameter
    estimates of the general cumulative model are mostly unidentifiable or
    at least only identifiable within a range of the entire parameter
    space. Thus, by maximizing a penalized rather than the usual
    non-penalized log-likelihood, this and other numerical problems common
    with the general model are to a large extent eliminated. Fitting is
    via a modified Newton's method. Several standard model performance and
    descriptive methods are also available. For more details on the penalty
    implemented here, see, Ugba (2021) <doi:10.21105/joss.03705> and 
    Ugba et al. (2021) <doi:10.3390/stats4030037>.
	"""
	
	homepage = "https://github.com/ejikeugba/serp"
	cran = "serp" 

	version("0.2.4", md5="499a867c0bfaf381e053ec0fdc26334d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ordinal@2016.12.12:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
