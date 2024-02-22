# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltmeta(RPackage):
	"""Alternative Meta-Analysis Methods

	Provides alternative statistical methods for meta-analysis, including:
 - bivariate generalized linear mixed models for synthesizing odds ratios, relative risks,
   and risk differences
   (Chu et al., 2012 <doi:10.1177/0962280210393712>)
 - heterogeneity tests and measures and penalization methods that are robust to outliers
   (Lin et al., 2017 <doi:10.1111/biom.12543>;
    Wang et al., 2022 <doi:10.1002/sim.9261>);
 - measures, tests, and visualization tools for publication bias or small-study effects
   (Lin and Chu, 2018 <doi:10.1111/biom.12817>;
    Lin, 2019 <doi:10.1002/jrsm.1340>;
    Lin, 2020 <doi:10.1177/0962280220910172>;
    Shi et al., 2020 <doi:10.1002/jrsm.1415>);
 - meta-analysis of diagnostic tests for synthesizing sensitivities, specificities, etc.
   (Reitsma et al., 2005 <doi:10.1016/j.jclinepi.2005.02.022>;
    Chu and Cole, 2006 <doi:10.1016/j.jclinepi.2006.06.011>);
 - meta-analysis methods for synthesizing proportions
   (Lin and Chu, 2020 <doi:10.1097/ede.0000000000001232>);
 - models for multivariate meta-analysis, measures of inconsistency degrees of freedom
   in Bayesian network meta-analysis, and predictive P-score
   (Lin and Chu, 2018 <doi:10.1002/jrsm.1293>;
    Lin, 2020 <doi:10.1080/10543406.2020.1852247>;
    Rosenberger et al., 2021 <doi:10.1186/s12874-021-01397-5>).
	"""
	
	cran = "altmeta" 

	version("4.1", md5="7d70e2a83779fdc338d57dbfe27e8aab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-metafor@3.0.2:", type=("build", "run"))
	depends_on("jags@4.0.0:4.999.999", type=("build", "link", "run"))
