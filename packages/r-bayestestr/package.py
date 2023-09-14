# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayestestr(RPackage):
    """Understand and Describe Bayesian Models and Posterior
Distributions
    
    Provides utilities to describe posterior
    distributions and Bayesian models. It includes point-estimates such as
    Maximum A Posteriori (MAP), measures of dispersion (Highest Density
    Interval - HDI; Kruschke, 2015 <doi:10.1016/C2012-0-00477-2>) and
    indices used for null-hypothesis testing (such as ROPE percentage, pd
    and Bayes factors). References: Makowski et al. (2021) <doi:10.21105/joss.01541>.
    """

    homepage = "https://cran.r-project.org/web/packages/bayestestR"
    
    cran = "bayestestR"

    # versions
    version("0.13.1", md5="ac9616d448c70b4793821597dbe23823")
    

    # dependencies
    depends_on("r@3.6:", type=('build', 'run'))
    depends_on("r-insight@0.19.1:", type=('build', 'run'))
    depends_on("r-datawizard@0.7.0:", type=('build', 'run'))
    
