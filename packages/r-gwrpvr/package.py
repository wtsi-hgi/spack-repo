# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwrpvr(RPackage):
	"""Genome-Wide Regression P-Value (Gwrpv)

	Computes the sample probability value (p-value)
    for the estimated coefficient from a standard
    genome-wide univariate regression.  It computes the exact
    finite-sample p-value under the assumption that the measured
    phenotype (the dependent variable in the regression) has
    a known Bernoulli-normal mixture distribution.
    Finite-sample genome-wide regression p-values (Gwrpv) with
    a non-normally distributed phenotype (Gregory Connor and
    Michael O'Neill, bioRxiv 204727 <doi:10.1101/204727>).
	"""
	
	homepage = "https://doi.org/10.1101/204727"
	cran = "gwrpvr" 

	version("1.0", md5="37d72a783f9d10fcc024bcbc42e83ba6")

