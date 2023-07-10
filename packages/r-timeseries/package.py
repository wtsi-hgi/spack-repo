# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeseries(RPackage):
    """Financial Time Series Objects (Rmetrics)
    
    'S4' classes and various tools for financial time series:
  Basic functions such as scaling and sorting, subsetting,
  mathematical operations and statistical functions.
    """

    homepage = "https://cran.r-project.org/web/packages/timeSeries"
    
    cran = "timeSeries"

    # versions
    version("4030.106", md5="dcdaf6115b1b45ab39254e83bc95078b")
    

    # dependencies
    depends_on("r-graphics", type=('build', 'run'))
    depends_on("r-gr-devices", type=('build', 'run'))
    
