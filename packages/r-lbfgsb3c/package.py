# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbfgsb3c(RPackage):
    """Limited Memory BFGS Minimizer with Bounds on Parameters with
optim() 'C' Interface

    Interfacing to Nocedal et al. L-BFGS-B.3.0
        (See <http://users.iems.northwestern.edu/~nocedal/lbfgsb.html>)
        limited memory BFGS minimizer with bounds on parameters.
        This is a fork of 'lbfgsb3'.
    This registers a 'R' compatible 'C' interface to L-BFGS-B.3.0 that uses the same
    function types and optimization as the optim() function (see writing 'R' extensions
        and source for details).  This package also adds more stopping criteria as well
        as allowing the adjustment of more tolerances.
    """
    
    homepage = "https://nlmixr2.github.io/lbfgsb3c/"
    cran = "lbfgsb3c" 

    version("3.4", sha256="f531b12d92ecbb0680fcf4ba29276428ee4a88184850ab52046f667da0624ab7")
    version("3.3", sha256="4d27d4dc9d5e22f1cb1e8aa06572f7e1e18f20f5c5217cd174e944174e893387")
    
    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-rcpp@0.12.3:", type=("build", "run"))
    depends_on("r-numderiv", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
