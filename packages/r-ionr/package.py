# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIonr(RPackage):
	"""Test for Indifference of Indicator

	Provides item exclusion procedure, which is a formal method to 
    test 'Indifference Of iNdicator' (ION). When a latent personality 
    trait-outcome association is assumed, then the association strength 
    should not depend on which subset of indicators (i.e. items) has been 
    chosen to reflect the trait. Personality traits are  often measured 
    (reflected) by  a sum-score of a certain set of indicators. 
    Item exclusion procedure randomly excludes items from a sum-score and 
    tests, whether the sum-score - outcome correlation changes. ION has been 
    achieved, when any item can be excluded from the sum-score without the 
    sum-score - outcome correlation substantially changing . For more details, 
    see Vainik, Mottus et. al, (2015) "Are Trait-Outcome Associations Caused
    by Scales or Particular Items? Example Analysis of Personality Facets and
    BMI",European Journal of Personality  DOI: <10.1002/per.2009> .
	"""
	
	homepage = "www.ut.ee/uku.vainik/ion/"
	cran = "ionr" 

	version("0.3.0", md5="c133618a53bede50191a42f39bd65dec")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
