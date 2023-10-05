# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinytest(RPackage):
    """Lightweight and Feature Complete Unit Testing Framework
    
    Provides a lightweight (zero-dependency) and easy to use 
    unit testing framework. Main features: install tests with 
    the package. Test results are treated as data that can be stored and 
    manipulated. Test files are R scripts interspersed with test commands, that
    can be programmed over. Fully automated build-install-test sequence for 
    packages. Skip tests when not run locally (e.g. on CRAN). Flexible and 
    configurable output printing. Compare computed output with output stored 
    with the package. Run tests in parallel. Extensible by other packages.
    Report side effects.
    """

    homepage = "https://cran.r-project.org/web/packages/tinytest"
    
    cran = "tinytest"

    # versions
    version("1.4.1", md5="e8d57668032bedd980cc9f1ad9c957d3")
    

    # dependencies
    depends_on("r@3.0.0:", type=('build', 'run'))
    
