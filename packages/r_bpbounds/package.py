# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpbounds(RPackage):
	"""Nonparametric Bounds for the Average Causal Effect Due to Balke
and Pearl and Extensions

	Implementation of the nonparametric bounds for the average
    causal effect under an instrumental variable model by Balke and Pearl
    (Bounds on Treatment Effects from Studies with Imperfect Compliance,
    JASA, 1997, 92, 439, 1171-1176). The package can calculate bounds for
    a binary outcome, a binary treatment/phenotype, and an instrument with
    either 2 or 3 categories. The package implements bounds for situations
    where these 3 variables are measured in the same dataset (trivariate
    data) or where the outcome and instrument are measured in one study
    and the treatment/phenotype and instrument are measured in another
    study (bivariate data).
	"""
	
	homepage = "https://github.com/remlapmot/bpbounds"
	cran = "bpbounds" 

	version("0.1.5", md5="50622349e8edca767f986350f02a4506")

	depends_on("r@3.5:", type=("build", "run"))
