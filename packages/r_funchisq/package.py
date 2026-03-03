# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunchisq(RPackage):
	"""Model-Free Functional Chi-Squared and Exact Tests

	Statistical hypothesis testing methods for
 inferring model-free functional dependency using asymptotic
 chi-squared or exact distributions. Functional test
 statistics are asymmetric and functionally optimal, unique
 from other related statistics. Tests in this package reveal
 evidence for causality based on the causality-by-
 functionality principle. They include asymptotic functional
 chi-squared tests (Zhang & Song 2013) <arXiv:1311.2707>,
 an adapted functional chi-squared test (Kumar & Song 2022) 
 <doi:10.1093/bioinformatics/btac206>, 
 and an exact functional test (Zhong & Song 2019)
 <doi:10.1109/TCBB.2018.2809743> (Nguyen et al. 2020)
 <doi:10.24963/ijcai.2020/372>. The normalized functional
 chi-squared test was used by Best Performer 'NMSUSongLab'
 in HPN-DREAM (DREAM8) Breast Cancer Network Inference
 Challenges (Hill et al. 2016) <doi:10.1038/nmeth.3773>. A
 function index (Zhong & Song 2019)
 <doi:10.1186/s12920-019-0565-9> (Kumar et al. 2018)
 <doi:10.1109/BIBM.2018.8621502> derived from the
 functional test statistic offers a new effect size measure
 for the strength of functional dependency, a better
 alternative to conditional entropy in many aspects. For
 continuous data, these tests offer an advantage over
 regression analysis when a parametric functional form
 cannot be assumed; for categorical data, they provide a
 novel means to assess directional dependency not possible
 with symmetrical Pearson's chi-squared or Fisher's exact
 tests.
	"""
	
	homepage = "https://www.cs.nmsu.edu/~joemsong/publications/"
	cran = "FunChisq" 

	version("2.5.3", md5="0c84b51e499478207f37e01c3e9f11e3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.6.1:", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
