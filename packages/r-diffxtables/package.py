# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffxtables(RPackage):
	"""Pattern Analysis Across Contingency Tables

	Statistical hypothesis testing of pattern heterogeneity
    via differences in underlying distributions across multiple
    contingency tables. Five tests are included: the comparative
    chi-squared test (Song et al. 2014) <doi:10.1093/nar/gku086>
    (Zhang et al. 2015) <doi:10.1093/nar/gkv358>, the Sharma-Song
    test (Sharma et al. 2021) <doi:10.1093/bioinformatics/btab240>, 
    the heterogeneity test, the marginal-change test (Sharma et al.
    2020) <doi:10.1145/3388440.3412485>, and the strength test
    (Sharma et al. 2020) <doi:10.1145/3388440.3412485>. Under the
    null hypothesis that row and column variables are statistically
    independent and joint distributions are equal, their test
    statistics all follow an asymptotically chi-squared distribution.
    A comprehensive type analysis categorizes the relation among the
    contingency tables into type null, 0, 1, and 2 (Sharma et al.
    2020) <doi:10.1145/3388440.3412485>. They can identify
    heterogeneous patterns that differ in either the first order
    (marginal) or the second order (differential departure from
    independence). Second-order differences reveal more
    fundamental changes than first-order differences across
    heterogeneous patterns.
	"""
	
	cran = "DiffXTables" 

	version("0.1.3", md5="792bce9e972c5c7edc80865d2327de28")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-rdpack@0.6.1:", type=("build", "run"))
