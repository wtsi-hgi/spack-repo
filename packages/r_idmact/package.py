# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdmact(RPackage):
	"""Interpreting Differences Between Mean ACT Scores

	Interpreting the differences between mean scale scores across various
    forms of an assessment can be challenging. This difficulty arises from different
    mappings between raw scores and scale scores, complex mathematical relationships,
    adjustments based on judgmental procedures, and diverse equating functions applied
    to different assessment forms. An alternative method involves running simulations
    to explore the effect of incrementing raw scores on mean scale scores. The
    'idmact' package provides an implementation of this approach based on the
    algorithm detailed in Schiel (1998)
    <https://www.act.org/content/dam/act/unsecured/documents/ACT_RR98-01.pdf> which
    was developed to help interpret differences between mean scale scores on the
    American College Testing (ACT) assessment. The function idmact_subj() within
    the package offers a framework for running simulations on subject-level scores.
    In contrast, the idmact_comp() function provides a framework for conducting
    simulations on composite scores.
	"""
	
	homepage = "https://github.com/mncube/idmact"
	cran = "idmact" 

	version("1.0.1", md5="560749b205e785d01384dd09075d68f8")

	depends_on("r-rlang", type=("build", "run"))
