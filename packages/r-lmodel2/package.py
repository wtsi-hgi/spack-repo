# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmodel2(RPackage):
    """Model II Regression
    
    Computes model II simple linear regression using ordinary
 least squares (OLS), major axis (MA), standard major axis (SMA), and
 ranged major axis (RMA).
    """

    homepage = "https://cran.r-project.org/web/packages/lmodel2"
    
    cran = "lmodel2"

    # versions
    version("1.7-3", md5="95346e8507abb2380049cc4c2ec18b65")
    

    # dependencies
    depends_on("r@2.14.0:", type=('build', 'run'))
    
