# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffectsize(RPackage):
    """Indices of Effect Size
    
    Provide utilities to work with indices of effect size for a wide 
    variety of models and hypothesis tests (see list of supported models using 
    the function 'insight::supported_models()'), allowing computation of and 
    conversion between indices such as Cohen's d, r, odds, etc.
    References: Ben-Shachar et al. (2020) <doi:10.21105/joss.02815>.
    """

    homepage = "https://cran.r-project.org/web/packages/effectsize"
    
    cran = "effectsize"

    # versions
    version("0.8.3", md5="2c9bab53476ab32a6954a162726cd3d3")
    

    # dependencies
    depends_on("r@3.6:", type=('build', 'run'))
    depends_on("r-bayestest-r@0.13.0:", type=('build', 'run'))
    depends_on("r-insight@0.18.8:", type=('build', 'run'))
    depends_on("r-performance@0.10.2:", type=('build', 'run'))
    depends_on("r-datawizard@0.6.5:", type=('build', 'run'))
    
