# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJfa(RPackage):
	"""Statistical Methods for Auditing

	Provides statistical methods for auditing as implemented in JASP
    for Audit (Derks et al., 2021 <doi:10.21105/joss.02733>). First, the package
    makes it easy for an auditor to plan a statistical sample, select the sample
    from the population, and evaluate the misstatement in the sample compliant
    with international auditing standards. Second, the package provides
    statistical methods for auditing data, including tests of digit
    distributions and repeated values. Finally, the package includes methods for
    auditing algorithms on the aspect of fairness and bias. Next to classical
    statistical methodology, the package implements Bayesian equivalents of
    these methods whose statistical underpinnings are described in Derks et al.
    (2021) <doi:10.1111/ijau.12240>, Derks et al. (2021)
    <doi:10.31234/osf.io/kzqp5>, and Derks et al. (2022)
    <doi:10.31234/osf.io/8nf3e>.
	"""
	
	homepage = "https://koenderks.github.io/jfa/"
	cran = "jfa" 

	version("0.7.0", md5="cf512f96cfd13b56fab2669a34fb3aaf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bde@1.0.1.1:", type=("build", "run"))
	depends_on("r-extradistr@1.9.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-truncdist@1.0.2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
