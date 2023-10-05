# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbitest(RPackage):
    """Testing DBI Backends
    
    A helper that tests DBI back ends for conformity
    to the interface.
    """

    homepage = "https://cran.r-project.org/web/packages/DBItest"
    
    cran = "DBItest"

    # versions
    version("1.7.3", md5="a43445d47911fa2d62ec63c653522354")
    

    # dependencies
    depends_on("r@3.2.0:", type=('build', 'run'))
    depends_on("r-blob@1.2.0:", type=('build', 'run'))
    depends_on("r-callr", type=('build', 'run'))
    depends_on("r-dbi@1.1.3:", type=('build', 'run'))
    depends_on("r-desc", type=('build', 'run'))
    depends_on("r-hms@0.5.0:", type=('build', 'run'))
    depends_on("r-lubridate", type=('build', 'run'))
    depends_on("r-palmerpenguins", type=('build', 'run'))
    depends_on("r-r6", type=('build', 'run'))
    depends_on("r-rlang@0.2.0:", type=('build', 'run'))
    depends_on("r-testthat@2.0.0:", type=('build', 'run'))
    depends_on("r-withr", type=('build', 'run'))
    depends_on("r-vctrs", type=('build', 'run'))
    
