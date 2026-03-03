# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesizemeans(RPackage):
	"""Sample Size Calculations for Normal Means

	Sample size requirements calculation
        using three different Bayesian criteria in the
        context of designing an experiment to estimate a normal mean or
        the difference between two normal means.  Functions for
        calculation of required sample sizes for the Average Length
        Criterion, the Average Coverage Criterion and the Worst Outcome
        Criterion in the context of normal means are provided.
        Functions for both the fully Bayesian and the mixed
        Bayesian/likelihood approaches are provided.
        For reference see Joseph L. and Bélisle P. (1997) <https://www.jstor.org/stable/2988525>.
	"""
	
	cran = "SampleSizeMeans" 

	version("1.2.3", md5="eb89cfe03bbcfe550ef34c883403fdee")

