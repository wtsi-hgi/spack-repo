# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxme(RPackage):
    """Mixed Effects Cox Models
    
    Fit Cox proportional hazards models containing both 
 fixed and random effects.  The random effects can have a general form, of which
 familial interactions (a "kinship" matrix) is a particular special case. 
 Note that the simplest case of a mixed effects Cox model, i.e. a single random 
 per-group intercept, is also called a "frailty" model.  The approach is based
 on Ripatti and Palmgren, Biometrics 2002.
    """

    homepage = "https://cran.r-project.org/web/packages/coxme"
    
    cran = "coxme"

    # versions
    version("2.2-18.1", md5="6f86a36d721b09094a926ceea3dba301")
    

    # dependencies
    depends_on("r-nlme", type=('build', 'run'))
    depends_on("r-matrix@1.0:", type=('build', 'run'))
    
