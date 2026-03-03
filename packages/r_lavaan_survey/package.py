# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RLavaanSurvey(RPackage):
    """Fit structural equation models (SEM) including factor analysis, multivariate regression models with latent variables and many other latent variable models while correcting estimates, standard errors, and chi-square-derived fit measures for a complex sampling design. Incorporate clustering, stratification, sampling weights, and finite population corrections into a SEM analysis. Wrapper around packages lavaan and survey."""

    homepage = "http://daob.nl/"
    cran = "lavaan.survey"

    version("1.1.3.1", sha256="b993a806e4f0f9cc9661c18eda989746707060cb2bd1cff997c603a091bf708c")
    version("1.1.3", sha256="f13eb7d95fabe28531bfadd9721342904da681a6173e0baf1a16de2c660350e6")
    version("1.1", sha256="ec13e0b514e477f872fd33b15fc8ce8312402c4e5ae877016093c6594cd84cef")
    version("1.0", sha256="a18aa442ff021f94bb85315490d3835c232d4cfee1b31b1c78c80eee18687ae3")
    version("0.8", sha256="9ac2228b90480df80f756aa55e1e3ac17baa9148dd628438fe93935c820c1e87")
    version("0.7", sha256="81800d243b7fce8a21abdaff4fd6a65539f06e0597614b2ce8303e684fd05e51")
    version("0.5", sha256="70d3493b71b2a64455f6d40841cbe7326dc85561e833f2b127d018f31f2c2edc")

    depends_on("r@2.14.0:", type=("build", "run"))
    depends_on("r-lavaan@0.5-20:", type=("build", "run"))
    depends_on("r-survey@3.30-3:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
