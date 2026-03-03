# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpow(RPackage):
	"""Computing the noncentrality parameter of the noncentral F
distribution

	Returns the noncentrality parameter of the noncentral F
        distribution if probability of type I and type II error,
        degrees of freedom of the numerator and the denominator are
        given.  It may be useful for computing minimal detectable
        differences for general ANOVA models.  This program is
        documented in the paper of A. Baharev, S. Kemeny, On the
        computation of the noncentral F and noncentral beta
        distribution; Statistics and Computing, 2008, 18 (3), 333-340.
	"""
	
	homepage = "http://dx.doi.org/10.1007/s11222-008-9061-3"
	cran = "fpow" 

	version("0.0-2", md5="605b0e97aee75f65bf1a0672cb4af607")

	depends_on("r@2.14.1:", type=("build", "run"))
