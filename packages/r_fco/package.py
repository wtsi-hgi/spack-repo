# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFco(RPackage):
	"""Flexible Cutoffs for Model Fit Evaluation in Covariance-Based
Structural Models

	A toolbox to derive flexible cutoffs for fit indices in 'Covariance-based Structural Equation Modeling' based on the paper by 'Niemand & Mai (2018)' <doi:10.1007/s11747-018-0602-9>. Flexible cutoffs are an alternative to fixed cutoffs - rules-of-thumb - regarding an appropriate cutoff for fit indices such as 'CFI' or 'SRMR'. It has been demonstrated that these flexible cutoffs perform better than fixed cutoffs in grey areas where misspecification is not easy to detect. The package provides an alternative to the tool at <https://flexiblecutoffs.org> as it allows to tailor flexible cutoffs to a given dataset and model, which is so far not available in the tool. The package simulates fit indices based on a given dataset and model and then estimates the flexible cutoffs. Some useful functions, e.g., to determine the 'GoF-' or 'BoF-nature' of a fit index, are provided. So far, additional options for a relative use (is a model better than another?) are provided in an exploratory manner.
	"""
	
	cran = "FCO" 

	version("0.8.0", md5="d2cd546a74a466b9025d20daf638a7d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-semtools", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
