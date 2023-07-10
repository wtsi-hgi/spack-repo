# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogitr(RPackage):
    """Logit Models w/Preference & WTP Space Utility Parameterizations
    
    Fast estimation of multinomial (MNL) and mixed logit (MXL) models in R. Models can be estimated using "Preference" space or "Willingness-to-pay" (WTP) space utility parameterizations. Weighted models can also be estimated. An option is available to run a parallelized multistart optimization loop with random starting points in each iteration, which is useful for non-convex problems like MXL models or models with WTP space utility parameterizations. The main optimization loop uses the 'nloptr' package to minimize the negative log-likelihood function. Additional functions are available for computing and comparing WTP from both preference space and WTP space models and for predicting expected choices and choice probabilities for sets of alternatives based on an estimated model. Mixed logit models can include uncorrelated or correlated heterogeneity covariances and are estimated using maximum simulated likelihood based on the algorithms in Train (2009) <doi:10.1017/CBO9780511805271>. More details can be found in Helveston (2023) <doi:10.18637/jss.v105.i10>.
    """

    homepage = "https://cran.r-project.org/web/packages/logitr"
    
    cran = "logitr"

    # versions
    version("1.1.0", md5="4ec266a8a3c2bd3d7656e276bfe0dada")
    

    # dependencies
    depends_on("r@3.5.0:", type=('build', 'run'))
    depends_on("r-generics", type=('build', 'run'))
    depends_on("r-m-a-s-s", type=('build', 'run'))
    depends_on("r-nloptr", type=('build', 'run'))
    depends_on("r-parallel", type=('build', 'run'))
    depends_on("r-randtoolbox", type=('build', 'run'))
    depends_on("r-tibble", type=('build', 'run'))
    
