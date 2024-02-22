# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComputeEs(RPackage):
	"""Compute Effect Sizes

	Several functions are available for calculating the most
    widely used effect sizes (ES), along with their variances, confidence
    intervals and p-values.  The output includes ES's of d (mean difference), g
    (unbiased estimate of d), r (correlation coefficient), z' (Fisher's z), and
    OR (odds ratio and log odds ratio). In addition, NNT (number needed to
    treat), U3, CLES (Common Language Effect Size) and Cliff's Delta are
    computed. This package uses recommended formulas as described in The
    Handbook of Research Synthesis and Meta-Analysis (Cooper, Hedges, &
    Valentine, 2009).
	"""
	
	homepage = "http://acdelre.com"
	cran = "compute.es" 

	version("0.2-5", md5="a8f4889ff9f35b81fcb53dd11030a4cd")

	depends_on("r@2.10.1:", type=("build", "run"))
